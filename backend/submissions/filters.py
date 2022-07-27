from multiprocessing import managers
from django.db import models

from rest_framework import filters

from authentification.models import Teacher

class SubmissionVisibleForTeacher(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):

        if request.user.is_superuser or view.action != 'list':
            return queryset

        students = request.user.teacher.get_students()
        return queryset.filter(submission__user__in=students)
