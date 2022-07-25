from multiprocessing import managers
from rest_framework import permissions

from authentification.models import Student

class CanReadProblem(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if not request.method in permissions.SAFE_METHODS:
            return False

        if request.user.is_teacher:
            return request.user in obj.managers.all()

        return False