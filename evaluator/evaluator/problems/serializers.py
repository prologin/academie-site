from rest_framework import serializers

from activities import validators

from problems import models


class ProblemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        allow_null=False,
        validators=[validators.slug_validator],
        allow_blank=False,
        label='title',
        write_only=True,
    )

    class Meta:
        model = models.Problem
        fields = (
            "title",
            "description",
            "subject",
            "difficulty",
            "allowed_languages",
            "skeletons",
            "author",
        )

        write_only_fields = (
            "tests",
            "correction_templates",
        )