from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=get_user_model().objects.all())]
            )

    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=get_user_model().objects.all())]
            )

    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
        )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        )
    
    birthdate = serializers.DateField(
        required=True,
        allow_null=False,
    )
    
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'birthdate',
            )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'birthdate': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthdate=validated_data['birthdate'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user