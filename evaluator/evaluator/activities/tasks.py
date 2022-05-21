from celery import shared_task
from problems.tasks import set_status
from problems.models import Problem
from django.core.cache import cache
from activities.models import Activity

import traceback

class ActivityException(Exception):
    pass

@shared_task(name="update_activity")
def update_activity(title, body, taskid):
    task = cache.get(taskid)
    if task is None:
        return
    try:
        activity, is_created = Activity.objects.update_or_create(
            title=title,
            defaults={
                'title': title,
                'description': body['description'],
                'opening': body['opening'],
                'closing': body['closing'],
                'publication': body['publication'],
            }
        )

        new_list = []
        for problem_slug in body['problems_slug']:
            problem = Problem.objects.get(title=problem_slug)
            new_list.append(problem)
        activity.problems.set(new_list)
        if not is_created:
            activity.version += 1
        activity.save()

    except:
        traceback.print_exc()
        set_status(task, "ERROR", "Failed to update or create the activity " + title)
        return
    set_status(task, "DONE", "")