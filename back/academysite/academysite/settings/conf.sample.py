from .common import *

DEBUG = True
CORS_ALLOW_ALL_ORIGINS = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

STATIC_URL = "/static/"

CORS_ALLOW_ALL_ORIGINS = DEBUG

ACADEMY_RESOURCES_PATH = "../../../academy-tracks"

CAMISOLE_URL = "http://vm.prologin.org"

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
