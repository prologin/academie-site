from authentification.permissions import TeacherPermission

from rest_framework import mixins, viewsets

from problems import tasks
from problems.filters import ProblemVisibleForTeacher
from problems.paginators import ProblemPagination
from problems.models import Problem
from problems.serializers import ProblemSerializer, ProblemListSerializer


class ProblemView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()
    pagination_class = ProblemPagination
    permission_classes = [TeacherPermission]
    filter_backends = [ProblemVisibleForTeacher]


    # destroy


    # create


    def perform_create(self, serializer):
        if self.request.user.email == 'mr.prologin@prologin.org':
            tasks.create_or_update_problem(serializer.validated_data)
        else:
            serializer.save().managers.add(self.request.user)


    # update


    # partial update


    def list(self, request, *args, **kwargs):
        self.serializer_class = ProblemListSerializer
        return super().list(request, *args, **kwargs)


    # retrieve