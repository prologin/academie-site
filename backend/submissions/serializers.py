from asyncore import read
from rest_framework import serializers

from submissions.models import ProblemSubmissionCode


class ProblemSubmissionCodeSerializer(serializers.ModelSerializer):

    problem_id = serializers.UUIDField(
        write_only=True,
    )

    activity_id = serializers.UUIDField(
        write_only=True,
    )

    class Meta:
        model = ProblemSubmissionCode
        fields = (
            "activity_id",
            "problem_id",
            "language",
            "code",
            "result",
        )

        read_only_fields = ("result", "validated", "date_submitted",)


class ProblemSubmissionCodeListSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='submission.user.email')
    problem_title = serializers.CharField(source='submission.problem.title')

    class Meta:
        model = ProblemSubmissionCode
        fields = (
            "id",
            "user_email",
            "language",
            "validated",
            "date_submitted",
            "problem_title",
        )