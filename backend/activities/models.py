import uuid

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from problems.models import Problem


class Difficulty(models.IntegerChoices):
    TRIVIAL = 0, _("trivial")
    EASY = 1, _("easy")
    MEDIUM = 2, _("medium")
    HARD = 3, _("hard")
    VERY_HARD = 4, _("very_hard")


def upload_image(instance, filename):
    return f"media/images/activities/{instance.id}.jpg"


class Activity(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    difficulty = models.PositiveSmallIntegerField(
        choices=Difficulty.choices,
    )

    title = models.CharField(
        validators=[RegexValidator("^[a-zA-Z0-9-_]{4,64}$")],
        max_length=64,
        unique=True,
    )

    author = models.CharField(
        max_length=150,
    )

    description = models.TextField()

    version = models.PositiveIntegerField(
        default=1,
    )

    problems = models.ManyToManyField(
        to=Problem,
    )

    image = ResizedImageField(
        blank=True,
        null=True,
        size=[600, 400],
        quality=75,
        crop=["middle", "center"],
        force_format="JPEG",
        keep_meta=False,
        upload_to=upload_image,
    )

    opening = models.DateTimeField(blank=True, null=True)
    closing = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField()

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


@receiver(models.signals.post_delete, sender=Activity)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)