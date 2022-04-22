from rest_framework import generics
from activities import models, serializers


class PublishedActivityList(generics.ListAPIView):
    serializer_class = serializers.PublishedActivitySerializer

    def get_queryset(self):
        return models.Activity.published_activities()


class PublishedActivityDetail(generics.RetrieveAPIView):
    serializer_class = serializers.DetailedPublishedActivitySerializer

    def get_queryset(self):
        return models.Activity.open_activities()
