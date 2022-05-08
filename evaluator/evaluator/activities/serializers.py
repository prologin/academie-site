from rest_framework import serializers
from activities import models, validators
from problems.models import Problem
from problems.validators import allowed_languages_validator
from problems.serializers import ProblemSerializer

class UpdateActivityRequestSerializer(serializers.Serializer):
    version = serializers.CharField(
        required=True,
        label="version",
        validators=[validators.commit_hash_validator],
        allow_null=False,
    )

    allowed_languages = serializers.ListField(
        required=True,
        label="allowed_languages",
        validators=[allowed_languages_validator],
        allow_null=False,
        min_length=1
    )

class PublishedActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = (
            "id",
            "slug",
            "title",
            "description",
            "author",
            "version",
            "opening",
            "closing",
            "publication",
        )


class DetailedPublishedActivitySerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)

    class Meta:
        model = models.Activity
        fields = (
            "id",
            "slug",
            "title",
            "description",
            "author",
            "version",
            "opening",
            "closing",
            "publication",
            "problems",
        )