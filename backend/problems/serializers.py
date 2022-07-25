from rest_framework import serializers

from problems import models

class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = (
            "id",
            "title",
            "difficulty",
            "allowed_languages",
            "author",
        )



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
            "author",
            "tests",
            "correction_templates",
        )

        extra_kwargs = {
            "tests": {"write_only": True},
            "correction_templates": {"write_only": True},
        }
