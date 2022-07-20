from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)

        token["username"] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, allow_null=False, allow_blank=False
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "birthdate",
            "accept_newsletter",
            "is_student",
            "is_teacher",
        )

        read_only_fields = (
            "is_student",
            "is_teacher",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = get_user_model()(**validated_data)
        user.set_password(password)
        user.save()
        return user
