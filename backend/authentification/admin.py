from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from authentification.forms import AdminProloginUserCreationForm, AdminProloginUserChangeForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = AdminProloginUserChangeForm
    add_form = AdminProloginUserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'birthdate', 'accept_newsletter')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'birthdate', 'accept_newsletter'),
        }),
    )



admin.site.register(User, UserAdmin)