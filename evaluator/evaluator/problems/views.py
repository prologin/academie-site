from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status

from problems import tasks
from problems.serializers import ProblemSerializer
from problems.models import Problem

from django.core.cache import cache

from status.models import Status
from status.serializers import StatusSerializer

from activities.validators import slug_validator
from activities.paginators import ActivityPagination


class ProblemView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    pagination_class = ActivityPagination
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()

    lookup_field = 'title'

    # get list
    
    def create(self, request):
        title = request.query_params.get('title')
        if title is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        task = tasks.update_problem.delay(title, request.data)
        cache.set(task.id, True)
        task_model = Status(id=task.id, status=task.status)


        serializer = StatusSerializer
        headers = self.get_success_headers(serializer.data)
        return Response(serializer(task_model).data, status=status.HTTP_201_CREATED, headers=headers)