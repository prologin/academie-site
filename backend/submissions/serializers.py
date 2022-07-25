from rest_framework import serializers

from activities.validators import slug_validator
from submissions.models import ProblemSubmission, ProblemSubmissionCode


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

        read_only_fields = ("result",)
