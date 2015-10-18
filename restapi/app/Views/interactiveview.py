import os
import json
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

__author__ = 'anubhaw'

BASE_DIR = os.getcwd() + "\\app\\static\\app\\content\\"

def interactive(request):
    modules = request.GET.getlist("module")
    links=[]
    for module in modules:
        links.append({"source":"RPi","target":module,"type":"ground"})
        links.append({"source":"RPi","target":module,"type":"signal"})
        links.append({"source":"RPi","target":module,"type":"power"})
    return render(request,"interactive.html",{"links":json.dumps(links, ensure_ascii=False)})


urlpatterns = [
    url(r'^.*$', interactive)
]