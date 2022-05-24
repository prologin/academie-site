from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from activities import paginators
from activities.models import Activity
from status.models import CeleryTaskStatus
from status.serializers import StatusSerializer
from activities.serializers import DetailedPublishedActivitySerializer, ActivitySerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from activities import tasks

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

        serializer_class = StatusSerializer
        task = CeleryTaskStatus(model_type="ACTIVITY")
        cache.set(task.id, task, 300)
        tasks.update_activity.delay(title, request.data, task.id)
        serializer = self.get_serializer()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer(task).data, status=status.HTTP_201_CREATED, headers=headers)

"""
class CreateUpdateActivity(generics.CreateAPIView):
    lookup_field = 'title'
    queryset = Activity.objects.all()

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


"""