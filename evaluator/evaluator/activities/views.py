from rest_framework import generics
from rest_framework.response import Response
from activities import models, serializers, paginators
from django import http


class ActivityDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.DetailedPublishedActivitySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Activity.published_activities()
    
    def patch(self, request, *args, **kwargs):
        return http.HttpResponseNotAllowed("PATCH not allowed")
    
    def put(self, request, *args, **kwargs):
        def get_queryset(self):
            return models.Activity.open_activities()
        obj = self.get_object()

        valid_ser = serializers.UpdateActivityRequestSerializer(data=request.data)
        if not valid_ser.is_valid():
            return http.HttpResponseBadRequest("Invalid request body")

        return Response(self.serializer_class(obj).data)



class PublishedActivityList(generics.ListAPIView):
    serializer_class = serializers.PublishedActivitySerializer
    pagination_class = paginators.ActivityPagination
    queryset = models.Activity.published_activities()
    
    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)