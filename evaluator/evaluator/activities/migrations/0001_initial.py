# Generated by Django 4.0.2 on 2022-03-17 13:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("problems", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        max_length=64,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z0-9-_]{4,64}$"
                            )
                        ],
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("version", models.CharField(max_length=384)),
                ("opening", models.DateTimeField(blank=True, null=True)),
                ("closing", models.DateTimeField(blank=True, null=True)),
                ("publication", models.DateTimeField()),
                (
                    "managers",
                    models.ManyToManyField(
                        blank=True, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "activities",
            },
        ),
        migrations.CreateModel(
            name="ActivityProblem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z0-9_-]{1,64}$"
                            )
                        ],
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="activities.activity",
                    ),
                ),
                (
                    "problem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="problems.problem",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "unique_together": {("activity", "slug")},
            },
        ),
        migrations.AddField(
            model_name="activity",
            name="problems",
            field=models.ManyToManyField(
                blank=True,
                through="activities.ActivityProblem",
                to="problems.Problem",
            ),
        ),
    ]
