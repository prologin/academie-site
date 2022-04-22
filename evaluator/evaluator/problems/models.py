from django.db import models
from django.utils.translation import gettext_lazy as _
from problems import validators
import uuid


class Difficulty(models.IntegerChoices):
    TRIVIAL = 0, _("trivial")
    EASY = 1, _("easy")
    MEDIUM = 2, _("medium")
    HARD = 3, _("hard")
    VERY_HARD = 4, _("very hard")


class Problem(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    title = models.CharField(
        max_length=150,
    )

    description = models.TextField()

    subject = models.TextField()

    difficulty = models.PositiveSmallIntegerField(choices=Difficulty.choices)

    allowed_languages = models.JSONField(
        validators=[validators.allowed_languages_validator],
    )

    scaffolds = models.JSONField(
        validators=[validators.language_string_mapping_validator],
        null=True,
        blank=True,
    )

    correction_templates = models.JSONField(
        validators=[validators.language_string_mapping_validator],
        null=True,
        blank=True,
    )

    tests = models.JSONField(
        validators=[validators.tests_validator],
    )

    def __str__(self):
        return str(self.id)
