from django.contrib.auth import get_user_model
from rest_framework import serializers

from reset.validators import email_exist

User = get_user_model()


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="email",
        required=True,
        validators=[email_exist],
    )


class ResetPasswordSerializerId(serializers.Serializer):
    password = serializers.CharField(
        label="password",
        required=True,
    )
