from rest_framework.parsers import JSONParser

from problems.models import Problem


class ProblemExecption(Exception):
    pass


def create_or_update_problem(title, body):
    problem, is_created = Problem.objects.update_or_create(
        title=title,
        defaults={
            "title": body["title"],
            "author": body["author"],
            "description": body["description"],
            "subject": body["subject"],
            "difficulty": body["difficulty"],
            "allowed_languages": body["allowed_languages"],
            "skeletons": body["skeletons"],
            "correction_templates": body["correction_templates"],
            "tests": body["tests"],
        },
    )

    return problem
