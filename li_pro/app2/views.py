from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import pymongo

# Create your views here.


class Test(View):

    def get(self, request):

        a = 1 + 3
        return HttpResponse(content=a)
