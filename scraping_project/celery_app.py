import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_project.settings')

app = Celery('scraping_app.tasks')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()