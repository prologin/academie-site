#!/bin/sh

exec docker-compose -p template exec backend_dev ./manage.py "$@"
