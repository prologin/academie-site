from uuid import uuid4
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models

app_name = "authentification"

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

    first_name = models.CharField(max_length=150, blank=False, null=False)

    last_name = models.CharField(max_length=150, blank=False, null=False)

    accept_newsletter = models.BooleanField(default=False)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = ProloginUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "birthdate",
        "first_name",
        "last_name",
        "username",
    ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    user = models.OneToOneField(ProloginUser, on_delete=models.CASCADE, primary_key=True)

    def get_teachers(self):
        teachers = set()
        for c in self.user.class_set.all():
            for t in c.teacher_set.all():
                teachers.add(t.user)
        return teachers

    def get_classes(self):
        classes = set()
        for c in self.class_set.all():
            classes.add(c)
        return classes

    def __str__(self):
        return str(self.user)


class Class(models.Model):
    class_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    students = models.ManyToManyField(to=get_user_model())
    name = models.CharField(max_length=64, default='Prologin class')

    def get_teachers(self):
        teachers = set()
        for t in self.teacher_set.all():
            teachers.add(t.user)
        return teachers 

    def __str__(self):
        return str(self.name)


class Teacher(models.Model):
    user = models.OneToOneField(ProloginUser, on_delete=models.CASCADE, primary_key=True)
    is_super_teacher = models.BooleanField(default=False)
    classes = models.ManyToManyField(Class)

    def get_students(self):
        students = set()
        for c in self.classes.all():
            for s in c.students.all():
                students.add(s.user)
        return students
    
    def __str__(self):
        return str(self.user)