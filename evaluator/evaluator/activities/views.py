from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from activities import paginators, tasks
from activities.models import Activity
from activities.serializers import DetailedPublishedActivitySerializer, ActivitySerializer

from status.serializers import StatusSerializer
from status.models import Status

from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

from datetime import datetime


class ActivityView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    pagination_class = paginators.ActivityPagination
    serializer_class = ActivitySerializer
    queryset = Activity.published_activities()

    lookup_field = 'title'

    # list get

    def retrieve(self, request, title=None): # get with parameter
        serializer_class = DetailedPublishedActivitySerializer
        return super().retrieve(request, title)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        title = request.query_params.get('title')
        if title is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.serializer_class = StatusSerializer

        task = tasks.update_activity.delay(title, request.data)
        cache.set(task.id, True)
        task_model = Status(id=task.id, status=task.status)

        serializer = self.get_serializer(task_model)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)