from authentification import models

from rest_framework import permissions

class CanReadActivity(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if not request.method in permissions.SAFE_METHODS:
            return False

        if request.user.is_student and obj.published:
            student_teachers = models.Student.objects.get(user=request.user).get_teachers()

            for t in obj.managers.all():
                if t in student_teachers:
                    return True

        elif request.user.is_teacher:
            return request.user in obj.managers.all()

        return False