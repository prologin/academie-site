from uuid import uuid4
from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from celery.result import AsyncResult

from status.serializers import StatusSerializer
from status.models import Status

from django.core.cache import cache


class StatusView(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def retrieve(self, request, pk=None):
        task = AsyncResult(id=pk)
        tmp = cache.get(pk)
        res = None
        if not (tmp is None):
            res = uuid4(tmp)

        obj = Status(id=task.id, status=task.status, result=res)
        if (cache.get(task.id) is None):
            obj.status = "NOT FOUND"
        serializer = self.get_serializer(obj)
        return Response(serializer.data)