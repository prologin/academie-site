from celery import shared_task
from celery.result import AsyncResult
from problems.models import Problem

from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

from rest_framework.parsers import JSONParser


class ProblemExecption(Exception):
    pass

@shared_task(name='test')
def test(a ,b):
    return a + b


@shared_task(name="update_problem")
def update_problem(slug, body):
    problem, is_created = Problem.objects.update_or_create(
        title=slug,
        defaults={
            'title': slug,
            'author': body['author'],
            'description': body['description'],
            'subject': body['subject'],
            'difficulty': body['difficulty'],
            'allowed_languages': body['allowed_languages'],
            'skeletons': body['skeletons'],
            'correction_templates': body['correction_templates'],
            'tests': body['tests']
        }
    )