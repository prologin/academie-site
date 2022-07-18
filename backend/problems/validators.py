from problems.languages import LANGUAGES
from django.core.exceptions import ValidationError


def allowed_languages_validator(data):
    if not isinstance(data, list):
        raise ValidationError("must be a list")

    for lang in data:
        if not isinstance(lang, str):
            raise ValidationError("languages must be strings")
        if lang not in LANGUAGES:
            raise ValidationError(f"{lang} is not a correct language")


def language_string_mapping_validator(data):
    if not isinstance(data, dict):
        raise ValidationError("must be a dict")
    for k, v in data.items():
        if not isinstance(k, str) or k not in LANGUAGES:
            raise ValidationError("invalid key")
        if not isinstance(v, str):
            raise ValidationError("values must be strings")


def tests_validator(data):
    if not isinstance(data, list):
        raise ValidationError("must be list")

    for test in data:
        if not isinstance(test, dict):
            raise ValidationError("must be dict")
        name = test.get("name")
        stdin = test.get("stdin")
        stdout = test.get("stdout")
        comment = test.get("comment")

        if any(
            v is None or not isinstance(v, str) for v in (name, stdin, stdout)
        ):
            raise ValidationError("invalid value")

        if comment is not None and not isinstance(comment, str):
            raise ValidationError("comment must be string")