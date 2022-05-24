from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status

from problems import tasks
from problems.serializers import ProblemSerializer
from problems.models import Problem

from django.core.cache import cache

from status import models
from status.serializers import StatusSerializer

from activities.validators import slug_validator
from activities.paginators import ActivityPagination

class ProblemView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    pagination_class = ActivityPagination
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()

    lookup_field = 'title'

    # get list
    
    def create(self, request):
        title = request.query_params.get('title')
        if title is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        task = models.CeleryTaskStatus(model_type="PROBLEM")
        cache.set(task.id, task, 300)
        tasks.update_problem.delay(title, request.data, task.id)

        serializer = StatusSerializer
        headers = self.get_success_headers(serializer.data)
        return Response(serializer(task).data, status=status.HTTP_201_CREATED, headers=headers)


"""

class ProblemCreateView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = StatusSerializer
    lookup_field = 'title'

    def post(self, request, title):
        valid_ser = UpdateProblemSerializer(data=request.data)
        if not valid_ser.is_valid():
            print(valid_ser.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            if not slug_validator(request.data['title']):
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        task = models.CeleryTaskStatus(model_type="PROBLEM")
        cache.set(task.id, task, 300)
        tasks.update_problem.delay(title, request.data, task.id)

        return Response(self.serializer_class(task).data)

    def get_queryset(self):
        return Problem.objects.all()

"""