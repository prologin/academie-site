from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from authentification.forms import (
    AdminProloginUserChangeForm,
    AdminProloginUserCreationForm,
)

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = AdminProloginUserChangeForm
    add_form = AdminProloginUserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "birthdate",
                    "accept_newsletter",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_student",
                    "is_teacher",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "birthdate",
                    "accept_newsletter",
                    "is_student",
                    "is_teacher",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
