from multiprocessing import managers
from authentification import models

from rest_framework import filters

class ProblemVisibleForTeacher(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser or view.action != 'list':
            return queryset
        elif request.user.is_teacher:
            return queryset.filter(managers__in=[request.user])
        
        return []
