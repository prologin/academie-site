import uuid

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from problems import validators


class Difficulty(models.IntegerChoices):
    TRIVIAL = 0, _("trivial")
    EASY = 1, _("easy")
    MEDIUM = 2, _("medium")
    HARD = 3, _("hard")
    VERY_HARD = 4, _("very_hard")


class Problem(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    title = models.CharField(
        max_length=64,
        validators=[RegexValidator("^[a-zA-Z0-9-_ ]{1,64}$")],
    )

    author = models.CharField(
        max_length=64,
    )

    managers = models.ManyToManyField(
        to=get_user_model(),
        blank=True,
    )

    description = models.TextField()

    subject = models.TextField()

    difficulty = models.PositiveSmallIntegerField(
        choices=Difficulty.choices,
    )

    allowed_languages = models.JSONField(
        validators=[validators.allowed_languages_validator],
    )

    skeletons = models.JSONField(
        validators=[validators.language_string_mapping_validator],
        blank=True,
    )

    correction_templates = models.JSONField(
        validators=[validators.language_string_mapping_validator],
        blank=True,
    )

    tests = models.JSONField(
        validators=[validators.tests_validator],
    )

    def isInPublishedActivity(self):
        pass


    def __str__(self):
        return str(self.title)
