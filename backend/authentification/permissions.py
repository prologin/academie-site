from rest_framework import permissions

class TeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active and (request.user.is_teacher or request.user.is_superuser):
            print("TEACHER")
            return True
        print("STUDENT")
        return False