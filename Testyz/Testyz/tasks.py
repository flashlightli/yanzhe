from celery import shared_task
import requests

@shared_task
def run_celery():
    requests.get('http://127.0.0.1:8802/api/hospital/publish')
    return {'run': 'OK'}