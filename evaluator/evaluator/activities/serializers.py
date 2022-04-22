from rest_framework import serializers
from activities import models
from problems.models import Problem


class PublishedActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = (
            "id",
            "slug",
            "title",
            "description",
            "opening",
            "closing",
            "publication",
        )


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = (
            "id",
            "title",
            "description",
            "difficulty",
        )


class DetailedPublishedActivitySerializer(serializers.ModelSerializer):
    problems = ProblemListSerializer(many=True)

    class Meta:
        model = models.Activity
        fields = (
            "id",
            "slug",
            "title",
            "description",
            "opening",
            "closing",
            "publication",
            "problems",
        )
