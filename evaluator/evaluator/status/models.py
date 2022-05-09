from django.db import models
import uuid


class CeleryTaskStatusModel(models.Model):

    MODEL_TYPE_CHOICES = (
        ("ACTIVITY", "Activity"),
        ("SUBMISSION", "Submission"),
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
        choices=MODEL_TYPE,
    )

    model_id = models.UUIDField()

    status = models.CharField(
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    info = models.TextField(
        default="",
        blank=True,
    )