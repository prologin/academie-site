# Academy-site backend

The backend of academy-site is a REST API built with django and django-rest-framework.

Here are the steps to run it locally

To enter the in the project run the following command

```
pipenv shell
```

Run the following commands

```
cd academysite
python ./manage.py migrate
```

Create a superuser to access the API

```
python ./manage.py createsuperuser
```

You need an accessible running server in order to effectively run submissions.
Once you configured this server, please enter its URI in settings.py : `CELERY_BROKER_URL`

Then open 2 terminals and run these commands in the first terminal :

```
pipenv shell
cd academysite
celery -A academysite worker -l INFO
```

and these commands in the second terminal:

```
pipenv shell
cd academysite
./manage.py runserver
```

And the server should be running