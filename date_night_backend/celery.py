import os

from django.conf import settings
from celery import Celery

app = Celery('date_night_backend')
app.conf.broker_url = settings.CELERY['broker_url']
app.conf.result_backend = settings.CELERY['result_backend']
app.conf.broker_transport_options = {
    'visibility_timeout': 43200
}

app.autodiscover_tasks(settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
