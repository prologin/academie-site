from rest_framework import serializers
from activities import models
from problems.models import Problem
from problems.serializers import ProblemSerializer


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