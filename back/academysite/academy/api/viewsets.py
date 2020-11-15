from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.urls import reverse
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from academy.models import TrackInstance, Submission
from academy.file_models import Problem
from . import serializers
    

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
            res = {'problem_id': p.id}
            res['properties'] = p.properties
            problems.append(res)
        return Response(problems)
    
    def retrieve(self, request, pk, track_pk):
        track_instance = self._get_track_instance(request, track_pk)
        problem = self._get_problem(track_instance.track_id, pk)
        res = {
            'problem_id': problem.id,
            'properties': problem.properties,
            'subject': problem.subject,
            'scaffold': problem.scaffold
        }

        if request.user.is_staff:
            res['template'] = problem.template
            res['tests'] = problem.tests
        
        return Response(res)
        