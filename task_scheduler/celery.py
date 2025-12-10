import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_scheduler.settings')
celery = Celery('task_scheduler')
celery.config_from_object('django.conf:settings', namespace = 'CELERY')
celery.autodiscover_tasks()