from rest_framework import permissions

def CanSubmitCode(request, activity):
    if request.user.is_superuser:
        return True

    classes = request.user.class_set.all()
    if request.user in activity.managers.all():
        return True
    elif activity.published and any(item in classes for item in activity.authorized_classes.all()):
        return True

    return False


class TeacherSubmissionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active and (request.user.is_teacher or request.user.is_superuser)


    def has_object_permission(self, request, view, obj):
        user = obj.submission.user
        teacher = request.user.teacher
        return user in teacher.get_students()