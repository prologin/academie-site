from celery import shared_task
from problems.models import Problem
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from rest_framework.parsers import JSONParser
from status.models import CeleryTaskStatus

from activities.models import ActivityProblem


class ProblemExecption(Exception):
    pass


def set_status(task, status, msg):
    task.status = status
    task.info = msg
    cache.set(task.id, task, 300)


@shared_task(name="update_problem")
def update_problem(slug, body, taskid):
    task = cache.get(taskid)
    try:
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

        if is_created:
            ActivityProblem.objects.create(
                problem=problem,
                slug=slug,
                order=0,
            )

        task.model_id = problem.id
    except Exception:
        set_status(task, "ERROR", "Failed to get or create the problem " + slug)
        return
    set_status(task, "DONE", "")