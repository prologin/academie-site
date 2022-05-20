from rest_framework import serializers
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.db import models

app_name = 'authentification'

class ProloginUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, birthdate, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, first_name, last_name, birthdate, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


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
    
    objects = ProloginUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['birthdate', 'first_name', 'last_name', 'username']