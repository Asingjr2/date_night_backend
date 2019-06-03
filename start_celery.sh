#!/usr/bin/env bash

celery -A date_night_backend worker --loglevel=info
