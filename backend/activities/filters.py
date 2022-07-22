from multiprocessing import managers
from authentification import models

from rest_framework import filters

class ActivityVisibleForUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser or view.action != 'list':
            return queryset
        elif request.user.is_teacher:
            return queryset.filter(managers__in=[request.user])
        elif request.user.is_student:
            student = models.Student.objects.get(user=request.user)
            teachers = list(student.get_teachers())

            return queryset.filter(published=True, managers__in=teachers)
        
        return []
