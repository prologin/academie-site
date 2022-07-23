from datetime import datetime

from rest_framework import serializers

from activities import models, validators
from activities.models import Activity
from problems.models import Problem
from problems.serializers import ProblemSerializer


class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ("image",)


class ActivitySerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        id_list = validated_data.pop('problems_id')
        activity = super().create(validated_data)
        activity.problems.set(list(Problem.objects.all().filter(id__in=id_list)))
        return activity

    problems_id = serializers.ListField(
        min_length=1,
        allow_null=False,
        validators=[validators.list_id_validator],
        label="problems_id",
        write_only=True,
    )

    title = serializers.CharField(
        allow_null=False,
        validators=[validators.slug_validator],
        label="title",
    )

    count = serializers.SerializerMethodField(
        read_only=True,
    )

    languages_list = serializers.SerializerMethodField(
        read_only=True,
    )

    def get_count(self, instance):
        return instance.problems.count()

    def get_languages_list(self, instance):
        languages = []
        for problem in instance.problems.all():
            for language in problem.allowed_languages:
                if not language in languages:
                    languages.append(language)
        return languages

    class Meta:
        model = models.Activity
        read_only_fields = ("image",)
        fields = (
            "id",
            "title",
            "opening",
            "closing",
            "problems_id",
            "count",
            "languages_list",
            "description",
            "author",
            "version",
            "image",
            "difficulty",
            "published",
        )
        extra_kwargs = {
            "description": {"write_only": True},
            "author": {"write_only": True},
            "version": {"write_only": True},
        }


class DetailedPublishedActivitySerializer(serializers.ModelSerializer):

    problems = ProblemSerializer(many=True)

    languages_list = serializers.SerializerMethodField(
        read_only=True,
    )

    def get_languages_list(self, instance):
        languages = []
        for problem in instance.problems.all():
            for language in problem.allowed_languages:
                if not language in languages:
                    languages.append(language)
        return languages

    class Meta:
        model = models.Activity
        fields = (
            "id",
            "title",
            "description",
            "author",
            "version",
            "opening",
            "closing",
            "published",
            "image",
            "problems",
            "languages_list",
            "difficulty",
        )
