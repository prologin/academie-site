from authentification.permissions import TeacherPermission
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from activities.paginators import ActivityPagination
from activities.permissions import CanReadActivity
from activities.filters import ActivityVisibleForUser
from activities.models import Activity
from activities.serializers import (
    ActivityImageSerializer,
    ActivitySerializer,
    DetailedPublishedActivitySerializer,
)

class ActivityImageView(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    #lookup_field = "title"
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

    pagination_class = ActivityPagination
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    filter_backends=[ActivityVisibleForUser]
    permission_classes_by_action = {
                                    'create': [TeacherPermission],
                                    'update': [TeacherPermission],
                                    'partial_update': [TeacherPermission],
                                    'destroy': [TeacherPermission],
                                    'retrieve': [CanReadActivity]
                                }

    # list


    # delete


    # update


    # partial_update


    # create

    def perform_create(self, serializer):
        serializer.save().managers.add(self.request.user)


    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = DetailedPublishedActivitySerializer
        return super().retrieve(request, *args, **kwargs)
    

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            return [permission() for permission in self.permission_classes]