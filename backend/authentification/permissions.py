from authentification import models

from rest_framework import permissions

class TeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active and (request.user.is_teacher or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return request.user in obj.managers.all() or request.user.is_superuser

class ReadActivityOrProblem(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if not request.method in permissions.SAFE_METHODS:
            return False

        if request.user.is_student:
            student_teachers = models.Student.objects.get(user=request.user).get_teachers()

            for t in obj.managers.all():
                if t in student_teachers:
                    return True

        elif request.user.is_teacher:
            return request.user in obj.managers.all()

        return False
