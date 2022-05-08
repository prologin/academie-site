from rest_framework import serializers
from activities import models, validators
from problems.models import Problem
from problems.serializers import ProblemSerializer

class UpdateActivityRequestSerializer(serializers.Serializer):
    version = serializers.CharField(required=True, label="version", validators=[validators.commit_hash_validator])

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