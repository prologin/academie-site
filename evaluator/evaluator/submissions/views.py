from rest_framework import mixins, viewsets
from rest_framework.response import Response

from submissions.models import ProblemSubmission, ProblemSubmissionCode
from submissions.serializers import ProblemSubmissionCodeSerializer
from submissions.tasks import run_code_submission

from problems.models import Problem

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class SubmissionView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProblemSubmissionCodeSerializer

    def create(self, serializer):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            problem = Problem.objects.get(title=request.data['title'])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        problem_submission = ProblemSubmission.objects.get_or_create(
            problem=problem,
            user=request.user,
            defaults={
                'problem': problem,
                'user': request.user,
            }
        )

        problem_submission_code = ProblemSubmissionCode.objects.create(
            submission=problem_submission,
            language=request.data['language'],
            code=request.data['code'],
            summary="Aurel c'est trop mon binome",
        )



        serializer_class = StatusSerializer
        task = CeleryTaskStatus(model_type="ACTIVITY")
        cache.set(task.id, task, 300)
        tasks.update_activity.delay(title, request.data, task.id)
        serializer = self.get_serializer()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer(task).data, status=status.HTTP_201_CREATED, headers=headers)

    pass