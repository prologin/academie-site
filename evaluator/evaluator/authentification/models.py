from rest_framework import serializers
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

from django.db import models

app_name = 'authentification'

class ProloginUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email, password, is_staff=False, is_superuser=False, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )


class ProloginUser(AbstractUser, PermissionsMixin):
    birthdate = models.DateField(
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        null=False,
    )

    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=False
        )

    last_name = models.CharField(
        max_length=150,
        blank=False,
        null=False
        )
    
    accept_newsletter = models.BooleanField(
        blank=False,
        null=False,
    )
    
    objects = ProloginUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['birthdate', 'first_name', 'last_name', 'username', 'accept_newsletter']