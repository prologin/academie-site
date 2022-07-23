import re

from rest_framework import serializers

from uuid import UUID

from problems.models import Problem


def commit_hash_validator(commit):
    if not re.match(r"^[a-f0-9]{7,32}$", commit):
        raise serializers.ValidationError(
            "The given string is not a hash commit"
        )
    return commit


def slug_validator(slug):
    if not re.match(r"^[a-zA-Z0-9-_ ]{1,64}$", slug):
        raise serializers.ValidationError("The given string is not a slug")
    return slug


def list_id_validator(l_id):
    if not isinstance(l_id, list):
        raise serializers.ValidationError("It has to be a list")
    for id in l_id:
        try:
            UUID(id, version=4)
        except ValueError:
            raise serializers.ValidationError(f"{id} is not a valid uuid4")
        if not Problem.objects.all().filter(id=id).exists():
            raise serializers.ValidationError(f"{id} does not exists")
    return l_id
