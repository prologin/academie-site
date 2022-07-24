from rest_framework import serializers

from activities import validators
from problems import models


class ProblemSerializer(serializers.ModelSerializer):
    '''
    title = serializers.CharField(
        allow_null=False,
        validators=[validators.slug_validator],
        allow_blank=False,
        label="title",
    )
    '''

    class Meta:
        model = models.Problem
        fields = (
            "id",
            "title",
            "description",
            "subject",
            "difficulty",
            "allowed_languages",
            "skeletons",
            "author",
            "tests",
            "correction_templates",
        )

        extra_kwargs = {
            "tests": {"write_only": True},
            "correction_templates": {"write_only": True},
        }
