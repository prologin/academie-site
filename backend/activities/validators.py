import re

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from problems.models import Problem


def commit_hash_validator(commit):
    if not re.match(r"^[a-f0-9]{7,32}$", commit):
        raise serializers.ValidationError(
            "The given string is not a hash commit"
        )
    return commit


def slug_validator(slug):
    if not re.match(r"^[a-zA-Z0-9-_]{4,64}$", slug):
        raise serializers.ValidationError("The given string is not a slug")
    return slug


def list_slug_validator(l_slug):
    if not isinstance(l_slug, list):
        raise serializers.ValidationError("It has to be a list")
    for slug in l_slug:
        slug_validator(slug)
        try:
            Problem.objects.get(title=slug)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(f"{slug} does not exists")
