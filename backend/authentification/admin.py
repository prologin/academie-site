from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from authentification import models
from authentification.forms import (
    AdminProloginUserChangeForm,
    AdminProloginUserCreationForm,
)

User = get_user_model()

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", "user_username", "user_email", "get_teachers",)

    search_fields = ("user", "user__username", "user_email",)

    autocomplete_fields = ['user']

    def user_username(self, student):
        return student.user.username

    def user_email(self, student):
        return student.user.email


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("user", "user_username", "user_email", "is_super_teacher",)

    search_fields = ("user", "user__username", "user_email", "classes__name",)

    autocomplete_fields = ['user']

    list_filter = ("is_super_teacher",)

    def user_username(self, teacher):
        return teacher.user.username

    def user_email(self, teacher):
        return teacher.user.email


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "get_teachers",)

    search_fields = ("name",)


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
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
