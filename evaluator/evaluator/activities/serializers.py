from rest_framework import serializers

from activities import models, validators
from activities.models import Activity

from problems.models import Problem
from problems.validators import allowed_languages_validator
from problems.serializers import ProblemSerializer

from django.core.exceptions import ValidationError

from datetime import datetime

class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = (
            "image",
        )


class ActivitySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        activity = Activity.objects.create(
            title=validated_data['title'],
            author=validated_data['author'],
            description=validated_data['description'],
            publication=validated_data['publication'],
            opening=validated_data['opening'],
            closing=validated_data['closing'],
        )

        new_list = []
        for problem_slug in validated_data['problems_slug']:
            problem = Problem.objects.get(title=problem_slug)
            new_list.append(problem)
        activity.problems.set(new_list)
        return activity


    problems_slug = serializers.ListField(
        min_length=1,
        allow_null=False,
        validators=[validators.list_slug_validator],
        label='problems_slug',
        write_only=True,
    )

    title = serializers.CharField(
        allow_null=False,
        validators=[validators.slug_validator],
        label='title',
    )

    count = serializers.SerializerMethodField(read_only=True,)

    languages_list = serializers.SerializerMethodField(read_only=True,)

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
        fields = (
            "id",
            "title",
            "opening",
            "closing",
            "problems_slug",
            "count",
            "languages_list",
            "description",
            "author",
            "version",
            "publication",
        )
        extra_kwargs = {
            "description": {'write_only': True},
            "author": {'write_only': True},
            "version": {'write_only': True},
            "publication": {'write_only': True}
        }


class DetailedPublishedActivitySerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)

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
            "publication",
            "problems",
        )