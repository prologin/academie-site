from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from problems import tasks
from problems.serializers import UpdateProblemSerializer
from problems.models import Problem

from django.core.cache import cache

from status import models
from status.serializers import StatusSerializer


class ProblemCreateView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = StatusSerializer
    lookup_field = 'title'

    def post(self, request, title):
        valid_ser = UpdateProblemSerializer(data=request.data)
        if not valid_ser.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        task = models.CeleryTaskStatus(model_type="PROBLEM")
        cache.set(task.id, task, 300)
        tasks.update_problem.delay(title, request.data, task.id)

        return Response(self.serializer_class(task).data)

    def get_queryset(self):
        return Problem.objects.all()