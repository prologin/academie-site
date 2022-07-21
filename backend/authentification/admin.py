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

    @admin.display(description='username')
    def user_username(self, student):
        return student.user.username

    @admin.display(description='email')
    def user_email(self, student):
        return student.user.email

    @admin.display(description='teachers')
    def get_teachers(self, student):
        return ", ".join(str(s) for s in student.get_teachers())


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("user", "user_username", "user_email", "is_super_teacher", "get_classes")

    search_fields = ("user", "user__username", "user_email", "classes__name",)

    autocomplete_fields = ['user']

    list_filter = ("is_super_teacher",)

    @admin.display(description='username')
    def user_username(self, teacher):
        return teacher.user.username

    @admin.display(description='email')
    def user_email(self, teacher):
        return teacher.user.email
    
    @admin.display(description='classes')
    def get_classes(self, teacher):
        return ", ".join(str(c) for c in teacher.classes.all())


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "get_teachers",)

    search_fields = ("name",)

    @admin.display(description='teachers')
    def get_teachers(self, _class):
        return ", ".join(str(t) for t in _class.get_teachers())


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
