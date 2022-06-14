from rest_framework import serializers

from activities import models, validators

from problems.models import Problem
from problems.validators import allowed_languages_validator
from problems.serializers import ProblemSerializer

from datetime import datetime

class ActivitySerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        time = datetime.now()
        if attrs['closing'] < attrs['opening']:
            attrs['closing'], attrs['opening'] = attrs['opening'], attrs['closing']
        
        return attrs

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
        write_only=True,
    )

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
            "problems_slug",
        )


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