from uuid import uuid4

from celery.result import AsyncResult
from django.core.cache import cache
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from status.models import Status
from status.serializers import StatusSerializer


class StatusView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def retrieve(self, request, pk=None):
        task = AsyncResult(id=pk)
        tmp = cache.get(pk)
        res = tmp

        obj = Status(id=task.id, status=task.status, result=res)
        if cache.get(task.id) is None:
            obj.status = "NOT FOUND"
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
