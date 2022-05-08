from django.db import models
from django.core.validators import RegexValidator
from problems.models import Problem
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid


class ActivityProblem(models.Model):
    problem = models.ForeignKey(
        to="problems.Problem",
        on_delete=models.CASCADE,
    )

    slug = models.CharField(
        validators=[RegexValidator("^[a-zA-Z0-9_-]{1,64}$")], max_length=64
    )

    activity = models.ForeignKey(
        to="activities.Activity",
        on_delete=models.CASCADE,
    )

    order = models.PositiveIntegerField()

    def __str__(self):
        return f"({self.order}) {self.slug} in {self.activity}"

    class Meta:
        unique_together = (("activity", "slug"),)
        ordering = ("order",)


class Activity(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    slug = models.CharField(
        validators=[RegexValidator("^[a-zA-Z0-9-_]{4,64}$")],
        max_length=64,
        unique=True,
    )

    author = models.CharField(
        max_length=150,
    )

    title = models.CharField(
        max_length=150,
    )

    description = models.TextField()

    version = models.CharField(
        validators=[RegexValidator("[a-f0-9]{7,}")],
        max_length=384,
    )

    problems = models.ManyToManyField(
        to=Problem,
        through=ActivityProblem,
        through_fields=("activity", "problem"),
        blank=True,
    )

    opening = models.DateTimeField(blank=True, null=True)
    closing = models.DateTimeField(blank=True, null=True)
    publication = models.DateTimeField()

    managers = models.ManyToManyField(
        to=get_user_model(),
        blank=True,
    )

    def __str__(self):
        return self.title

    @classmethod
    def notCloseActivities(cls):
        return cls.objects.filter(
            models.Q(
                closing_isnull=False,
                closing__gte=timezone.now(),
            )
        )

    @classmethod
    def published_activities(cls):
        return cls.objects.filter(publication__lte=timezone.now())

    @classmethod
    def open_activities(cls):
        now = timezone.now()
        return cls.published_activities().filter(
            models.Q(
                opening__isnull=False,
                closing__isnull=False,
                opening__lte=now,
                closing__gte=now,
            )
            | models.Q(
                opening=None,
                closing__isnull=False,
                closing__gte=now
            )
            | models.Q(
                opening__isnull=False, 
                closing=None, 
                opening__lte=now)
            | models.Q(
                opening__isnull=True,
                closing__isnull=True
            )
        )

    class Meta:
        verbose_name_plural = "activities"
