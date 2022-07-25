from activities.models import Activity
from problems.models import Problem

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status

from status.models import Status
from status.serializers import StatusSerializer
from submissions.models import ProblemSubmission, ProblemSubmissionCode
from submissions.serializers import ProblemSubmissionCodeSerializer
from submissions.tasks import run_code_submission

User = get_user_model()

'''
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
'''

class SubmissionView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProblemSubmissionCodeSerializer
    queryset = ProblemSubmissionCode.objects.all()
#    lookup_field = "id"

#    def retrieve(self, request, id=None):  # get with parameter


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        activity = get_object_or_404(Activity, id=serializer.validated_data['activity_id'])
        if not activity.problems.all().filter(id__in=[serializer.validated_data['problem_id']]).exists():
            return Response(status=status.HTTP_404_NOT_FOUND, data={"Detail": "The problem is not part of the activity"})
        problem = Problem.objects.get(id=serializer.validated_data['problem_id'])
        if not serializer.validated_data['language'] in problem.allowed_languages:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Detail": "This language is not available for the problem"})
        
        problem_submission, _ = ProblemSubmission.objects.get_or_create(
            problem=problem,
            user=self.request.user,
            defaults={
                "problem": problem,
                "user": self.request.user,
            },
        )

        correction_template = ""

        try:
            correction_template += problem.correction_templates[
                serializer.validated_data["language"]
            ]
        except:
            correction_template = ""

        problem_submission_code = ProblemSubmissionCode.objects.create(
            submission=problem_submission,
            language=serializer.validated_data["language"],
            code=serializer.validated_data["code"] + "\n\n\n\n\n" + correction_template,
            summary="Aurel c'est trop mon binome",
        )

        self.serializer_class = StatusSerializer

        task = run_code_submission.delay(problem_submission_code.id)
        cache.set(task.id, problem_submission_code.id)
        task_model = Status(
            id=task.id, status=task.status, result=problem_submission_code.id
        )

        serializer = self.get_serializer(task_model)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
