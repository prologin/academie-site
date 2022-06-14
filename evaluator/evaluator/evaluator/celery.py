import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evaluator.settings.dev")

app = Celery("evaluator")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

#app.result_expires = 10

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app.conf.broker_url = BASE_REDIS_URL

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'