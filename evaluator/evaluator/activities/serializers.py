from rest_framework import serializers
from activities import models, validators
from problems.models import Problem
from problems.validators import allowed_languages_validator
from problems.serializers import ProblemSerializer

class CreateUpdateActivitySerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=64,
        required=True,
        allow_null=False,
        allow_blank=False,
        label="title",
    )

    description = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        label='description',
    )

    opening = serializers.DateTimeField(
        allow_null=False,
        label='opening',
    )

    closing = serializers.DateTimeField(
        allow_null=False,
        label='closing',
    )

    publication = serializers.DateTimeField(
        allow_null=False,
        label='publication',
    )

    problems_slug = serializers.ListField(
        min_length=1,
        allow_null=False,
        validators=[validators.list_slug_validator],
        label='problems_slug',
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