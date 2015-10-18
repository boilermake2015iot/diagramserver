import os

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

__author__ = 'anubhaw'

def index(request):
    return render(request,"index.html")

urlpatterns = [
    url(r'^.*$', index)
]
