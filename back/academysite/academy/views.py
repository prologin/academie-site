from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from academy.models import TrackInstance, Submission, Validators
from academy.file_models import Problem
from . import serializers
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from academy import tasks
from django.utils import timezone
from django.contrib.auth import get_user_model


class SubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SubmissionSerializer

    def _can_run_submission(self, request, pk):
        submission = Submission.objects.get(pk=pk)
        return (
            submission.track.public and submission.author == self.request.user
        ) or self.request.user.is_staff

    @action(detail=True, methods=["post"])
    def run(self, request, pk):
        try:
            if self._can_run_submission(request, pk):
                tasks.run_code_submission.apply_async(args=[pk])
                return Response(
                    {"status_message": "Submission sent to correction"}
                )
        except ObjectDoesNotExist:
            raise Http404
        raise Http404

    def perform_update(self, serializer):
        serializer.instance.submission_count += 1
        serializer.instance.submission_date = timezone.now()
        self.perform_create(serializer)

    def perform_create(self, serializer):
        try:
            Validators.validate_problem(
                serializer.validated_data["track"].track_id,
                serializer.validated_data["problem_id"],
            )
        except:
            raise ValidationError(
                f"No problem with given id in selected track."
            )
        serializer.save(
            author=self.request.user, submission_date=timezone.now()
        )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Submission.objects.all()
        return Submission.objects.filter(
            author=self.request.user, track__public=True
        )


class TrackInstanceViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_staff:
            return serializers.TrackInstanceStaffSerializer
        return serializers.TrackInstanceSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return TrackInstance.objects.all()
        return TrackInstance.objects.filter(public=True)


class ProblemViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def _get_related_user_submission(self, user, track, problem):
        try:
            return Submission.objects.get(
                track=track, author=user, problem_id=problem.id
            ).id
        except ObjectDoesNotExist:
            return None

    def _get_track_instance(self, request, track_pk):
        try:
            track_instance = TrackInstance.objects.get(pk=track_pk)
            if not (request.user.is_staff or track_instance.public):
                raise Http404
            return track_instance
        except ObjectDoesNotExist:
            raise Http404

    def _get_problem(self, track_id, problem_id):
        problem = Problem(track_id, problem_id)
        if not problem.is_valid():
            raise Http404
        return problem

    def list(self, request, track_pk):
        track_instance = self._get_track_instance(request, track_pk)
        problems = []
        for p in track_instance.track.problems:
            res = {"problem_id": p.id}
            res["properties"] = p.properties
            res["solved"] = self._get_related_user_submission(
                request.user, track_instance, p
            )
            problems.append(res)
        return Response(problems)

    def retrieve(self, request, pk, track_pk):
        track_instance = self._get_track_instance(request, track_pk)
        problem = self._get_problem(track_instance.track_id, pk)
        user_submission_id = self._get_related_user_submission(
            request.user, track_instance, problem
        )
        res = {
            "problem_id": problem.id,
            "properties": problem.properties,
            "subject": problem.subject,
            "scaffold": problem.scaffold,
            "submission": user_submission_id,
        }

        if request.user.is_staff:
            res["template"] = problem.template
            res["tests"] = problem.tests

        return Response(res)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        User = get_user_model()
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.none()

    @action(detail=False)
    def me(self, request):
        return Response(self.serializer_class(request.user).data)
