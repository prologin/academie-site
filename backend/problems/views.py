from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from activities.paginators import ActivityPagination
from activities.validators import slug_validator
from problems import tasks
from problems.models import Problem
from problems.serializers import ProblemSerializer


class ProblemView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    pagination_class = ActivityPagination
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()

    lookup_field = "title"

    def create(self, request):
        title = request.query_params.get("title")
        if title is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
            )

        obj = tasks.create_or_update_problem(title, request.data)
        serializer = self.get_serializer(data=obj)
        serializer.is_valid()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
