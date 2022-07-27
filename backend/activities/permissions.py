from authentification import models

from rest_framework import permissions

class CanReadActivity(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if not request.method in permissions.SAFE_METHODS:
            return False

        classes = request.user.class_set.all()
        if request.user in obj.managers.all():
            return True
        elif obj.published and any(item in classes for item in obj.authorized_classes.all()):
            return True

        return False