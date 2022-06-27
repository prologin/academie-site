from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.response import Response

from submissions.models import ProblemSubmission, ProblemSubmissionCode
from submissions.serializers import ProblemSubmissionCodeSerializer
from submissions.tasks import run_code_submission

from problems.models import Problem

from status.serializers import StatusSerializer
from status.models import Status

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

from django.shortcuts import get_object_or_404

User = get_user_model()

class SubmissionView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProblemSubmissionCodeSerializer
    queryset = ProblemSubmissionCode.objects.all()

    def retrieve(self, request, id=None): # get with parameter
        return super().retrieve(request, id)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        problem = get_object_or_404(Problem, title=request.data['title'])
 
        problem_submission, _ = ProblemSubmission.objects.get_or_create(
            problem=problem,
            user=request.user,
            defaults={
                'problem': problem,
                'user': request.user,
            }
        )

        correction_template = ""

        try:
            correction_template += problem.correction_templates[request.data['language']]
        except:
            correction_template = ""

        problem_submission_code = ProblemSubmissionCode.objects.create(
            submission=problem_submission,
            language=request.data['language'],
            code=request.data['code'] + "\n\n\n\n\n" + correction_template,
            summary="Aurel c'est trop mon binome",
        )

        self.serializer_class = StatusSerializer

        task = run_code_submission.delay(problem_submission_code.id)
        cache.set(task.id, True)
        task_model = Status(id=task.id, status=task.status, result=problem_submission_code.id)

        serializer = self.get_serializer(task_model)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)