from django.core.exceptions import ObjectDoesNotExist
from authentification.permissions import TeacherPermission
from rest_framework import mixins, status, viewsets
from rest_framework import generics
from rest_framework.response import Response

from activities import paginators
from activities.models import Activity
from activities.serializers import (
    ActivityImageSerializer,
    ActivitySerializer,
    DetailedPublishedActivitySerializer,
)

class ActivityImageView(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    lookup_field = "title"
    serializer_class = ActivityImageSerializer
    queryset = Activity.objects.all()
    permission_classes = [TeacherPermission]


    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        obj.image = request.FILES["image"]
        obj.save()

        return Response(status=status.HTTP_200_OK)


class ActivityView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    pagination_class = paginators.ActivityPagination
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes_by_action = {
                                    'create': [TeacherPermission],
                                    'update': [TeacherPermission],
                                    'partial_update': [TeacherPermission],
                                    'destroy': [TeacherPermission],
                                    'retrieve': []
                                }

    lookup_field = "title"

    # list get

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            _ = Activity.objects.get(title=request.data["title"])
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return super().create(request, *args, **kwargs)

    def retrieve(self, request, title=None):  # get with parameter
        self.serializer_class = DetailedPublishedActivitySerializer
        return super().retrieve(request, title)
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            return [permission() for permission in self.permission_classes]