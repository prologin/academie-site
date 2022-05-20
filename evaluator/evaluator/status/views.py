from rest_framework import generics
from rest_framework.response import Response
from status import models, serializers
from django.core.cache import cache
from django import http

class StatusRetrieve(generics.RetrieveAPIView):
    serializer_class = serializers.StatusFullSerializer

    def get(self, request, id):
        task = cache.get(id)
        if task is None:
            return http.Http404()
        return Response(self.serializer_class(task).data)