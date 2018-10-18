from django.views.generic import View
from django.http import HttpResponse
from Testyz.tasks import run_celery

class A(View):

    def get(self, requests):
        run_celery()
        return HttpResponse(content='ok')