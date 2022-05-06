from rest_framework import generics
from activities import models, serializers, paginators

class PublishedActivityDetail(generics.RetrieveAPIView):
    serializer_class = serializers.DetailedPublishedActivitySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Activity.open_activities()



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