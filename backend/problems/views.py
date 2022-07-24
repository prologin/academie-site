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
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()


    # destroy


    # create

    def perform_create(self, serializer):
        if self.request.user.email == 'mr.prologin@prologin.org':
            tasks.create_or_update_problem(serializer.validated_data)
        else:
            serializer.save()


    # update


    # partial update