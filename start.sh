#!/usr/bin/env bash

set -e

python /code/manage.py migrate --noinput
python /code/manage.py collectstatic --noinput
gunicorn date_night_backend.wsgi:application --bind 0.0.0.0:8082 --reload
