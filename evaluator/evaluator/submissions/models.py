from django.contrib.auth import get_user_model
from django.db import models
from problems.languages import LANGUAGES
import uuid

LANGUAGE_CHOICES = tuple((lang, lang) for lang in LANGUAGES)


class ProblemSubmission(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    problem = models.ForeignKey(
        to="activities.ActivityProblem",
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    validated = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    validated_at = models.DateTimeField(null=True, blank=True)

    validated_by = models.OneToOneField(
        to="submissions.ProblemSubmissionCode",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user}: {self.problem}"

    class Meta:
        unique_together = (("problem", "user"),)


class ProblemSubmissionCode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    submission = models.ForeignKey(
        to="submissions.ProblemSubmission",
        on_delete=models.CASCADE,
    )

    language = models.CharField(
        max_length=32,
        choices=LANGUAGE_CHOICES,
    )

    code = models.TextField()

    summary = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    date_submitted = models.DateTimeField(auto_now_add=True)

    date_corrected = models.DateTimeField(null=True, blank=True)

    result = models.JSONField(null=True, blank=True)

    validated = models.BooleanField(default=False, editable=True)

    def __str__(self):
        return str(self.id)
