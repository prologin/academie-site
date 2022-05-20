from rest_framework import serializers
from problems import models

class ProblemSerializer(serializers.ModelSerializer):
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
        )

class UpdateProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = (
            "title",
            "allowed_languages",
            "tests",
            "skeletons",
            "correction_templates",
            "author",
            "description",
            "subject",
            "difficulty",
        )