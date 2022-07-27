from multiprocessing import managers
from django.db import models

from rest_framework import filters

class ActivityVisibleForUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser or view.action != 'list':
            return queryset

        classes = list(request.user.class_set.all())
        return queryset.filter(
            models.Q(managers__in=[request.user]) | models.Q(authorized_classes__in=classes)
        ).distinct()
