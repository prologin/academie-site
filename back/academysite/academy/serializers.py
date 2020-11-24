from rest_framework import serializers
from django.contrib.auth import get_user_model
from academy import models


class TrackInstanceStaffSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField("get_properties")

    def get_properties(self, obj):
        return obj.track.properties

    class Meta:
        model = models.TrackInstance
        fields = "__all__"


class TrackInstanceSerializer(TrackInstanceStaffSerializer):
    class Meta:
        model = models.TrackInstance
        fields = ("name", "id", "public", "properties")


class SubmissionSerializer(serializers.ModelSerializer):
    class TrackSelectField(serializers.PrimaryKeyRelatedField):
        def get_queryset(self):
            if self.context["request"].user.is_staff:
                return models.TrackInstance.objects.all()
            return models.TrackInstance.objects.filter(public=True)

    track = TrackSelectField()

    class Meta:
        model = models.Submission
        fields = (
            "track",
            "problem_id",
            "code",
            "id",
            "author",
            "submission_date",
            "correction_date",
            "submission_count",
            "correction_count",
            "passed",
            "correction_data",
        )
        read_only_fields = (
            "id",
            "author",
            "submission_date",
            "correction_date",
            "submission_count",
            "correction_count",
            "passed",
            "correction_data",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "groups",
            "is_staff",
        )
