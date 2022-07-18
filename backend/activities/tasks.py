from celery import shared_task

from problems.models import Problem

from activities.models import Activity

class ActivityException(Exception):
    pass


@shared_task(name="update_activity")
def update_activity(title, body):
    activity, is_created = Activity.objects.update_or_create(
        title=title,
        defaults={
            'title': body['title'],
            'description': body['description'],
            'opening': body['opening'],
            'closing': body['closing'],
            'publication': body['publication'],
            'author': body['author'],
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