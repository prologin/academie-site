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