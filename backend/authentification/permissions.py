from rest_framework import permissions

class TeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active and (request.user.is_teacher or request.user.is_superuser)


    def has_object_permission(self, request, view, obj):
        return request.user in obj.managers.all() or request.user.is_superuser