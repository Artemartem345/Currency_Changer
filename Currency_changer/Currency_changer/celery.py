import os
from celery import Celery
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Currency_changer.settings")

app = Celery('Currency_changer')

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()