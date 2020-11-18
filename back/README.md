# Prologin Academy Backend

This websites uses django and django-rest-framework for its backend.

## Virtualenv and Dependencies

Installation

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Every time you want to run the project

```
source .venv/bin/activate
```

## Academy resources

In order to work properly this website needs an auxiliary repository containing
all the problems (and tests) and tacks.

You can clone an example Academy Resources with this command :

```
git clone https://gitlab.com/lportemo/academy-tracks
```

By default the site looks for a folder called academy-tracks in '../..' (relative to this README)

## Configuration Environment

The default Django settings module is academysite.settings.dev.
A generic working settings file is available in academysite/academysite/settings/conf.sample.py.

You may want to copy it :

```
cp academysite/academysite/settings/{conf.sample,dev}.py
```

## Redis server (required to correct submissions)

Celery uses redis as its backend. If you have docker installed on your machine
you can run a local redis server with :

```
docker run --name prologin-academy_redis -d -p 6379:6379 redis:alpine
```

## Run the server

Start the server itself

```
cd academysite
./manage.py runserver
```

And in another terminal, start the celery worker (redis server required):

```
cd academysite
celery -A academysite worker -E -l info
```

## Tools
API Documentation is available at https://127.0.0.1:8000/api/doc