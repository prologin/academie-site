from django.db import models
import uuid

app_name = "status"

class CeleryTaskStatus(models.Model):
    class Meta:
        managed = False

    MODEL_TYPE_CHOICES = (
        ("ACTIVITY", "Activity"),
        ("SUBMISSION", "Submission"),
        ("PROBLEM", "Problem"),
    )

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("DONE", "Done"),
        ("ERROR", "Error"),
    )

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    model_type = models.CharField(
        choices=MODEL_TYPE_CHOICES,
        max_length=64,
    )

    model_id = models.UUIDField()

    status = models.CharField(
        choices=STATUS_CHOICES,
        default="PENDING",
        max_length=64,
    )

    info = models.TextField(
        default="",
        blank=True,
    )