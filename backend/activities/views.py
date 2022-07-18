from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from activities import paginators, tasks
from activities.models import Activity
from activities.serializers import DetailedPublishedActivitySerializer, ActivitySerializer, ActivityImageSerializer

from status.serializers import StatusSerializer
from status.models import Status

from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

from datetime import datetime

import os

class ActivityImageView(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    lookup_field = 'title'
    serializer_class = ActivityImageSerializer
    queryset = Activity.objects.all()

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        path = f'./uploads/images/activities/{obj.id}.jpg'
        if os.path.exists(path):
            os.remove(path)

        obj.image = request.FILES['image']
        obj.save()

        return Response(status=status.HTTP_200_OK)



class ActivityView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    pagination_class = paginators.ActivityPagination
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()

    lookup_field = 'title'

    # list get

    def create(self, request, *args, **kwargs):
        try:
            _ = Activity.objects.get(title=request.data['title'])
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return super().create(request, *args, **kwargs)


    def retrieve(self, request, title=None): # get with parameter
        self.serializer_class = DetailedPublishedActivitySerializer
        return super().retrieve(request, title)