def CanSubmitCode(request, activity):
    if request.user.is_superuser:
        return True

    classes = request.user.class_set.all()
    if request.user in activity.managers.all():
        return True
    elif activity.published and any(item in classes for item in activity.authorized_classes.all()):
        return True

    return False