from rest_framework import serializers

from submissions.models import ProblemSubmission, ProblemSubmissionCode

from activities.validators import slug_validator

class ProblemSubmissionCodeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        validators=[slug_validator],
        label='title',
        required=True,
        write_only=True,
    )

    class Meta:
        model = ProblemSubmissionCode
        fields = (
            "title",
            "language",
            "code",
        )