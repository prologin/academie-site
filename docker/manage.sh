#!/bin/sh

exec docker exec -it docker_backend_dev_1 ./manage.py "$@"
