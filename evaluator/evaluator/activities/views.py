from rest_framework import generics
from rest_framework.response import Response
from activities import paginators
from activities.models import Activity
from status.models import CeleryTaskStatus
from status.serializers import StatusSerializer
from activities.serializers import DetailedPublishedActivitySerializer, PublishedActivitySerializer, CreateUpdateActivitySerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from activities import tasks

from datetime import datetime

class ActivityDetail(generics.RetrieveUpdateAPIView):
    serializer_class = DetailedPublishedActivitySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Activity.published_activities()
    
    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def put(self, request, *args, **kwargs):
        def get_queryset(self):
            return models.Activity.open_activities()
        obj = self.get_object()

        return Response(self.serializer_class(obj).data)


class PublishedActivityList(generics.ListAPIView):
    serializer_class = PublishedActivitySerializer
    pagination_class = paginators.ActivityPagination
    queryset = Activity.published_activities()
    
    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CreateUpdateActivity(generics.CreateAPIView):
    lookup_field = 'title'

    def get_queryset(self):
        return Activity.objects.all()
    
    def post(self, request, title):
        valid_ser = CreateUpdateActivitySerializer(data=request.data)
        if not valid_ser.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        body = request.data
        time = datetime.now()
        if body['closing'] <= body['opening'] or body['publication'] > body['opening']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        task = CeleryTaskStatus(model_type="ACTIVITY")
        cache.set(task.id, task, 300)
        tasks.update_activity.delay(title, request.data, task.id)

        return Response(status=status.HTTP_201_CREATED)


