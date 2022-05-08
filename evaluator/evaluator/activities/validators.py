from rest_framework import serializers
import re

def commit_hash_validator(commit):
    if not re.match(r'^[a-f0-9]{7,32}$', commit):
        raise serializers.ValidationError("The given string is not a hash commit")
    return commit