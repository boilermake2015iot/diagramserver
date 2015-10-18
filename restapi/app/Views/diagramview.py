import os

from django.conf.urls import url
from django.http import HttpResponse
from PIL import Image

__author__ = 'anubhaw'

BASE_DIR = os.getcwd() + "\\app\\static\\app\\content\\"


def diagram(request):
    modules = request.GET.getlist("module")
    im = Image.new("RGBA", (864, 864))
    for module in modules:
        try:
            image = Image.open(BASE_DIR +  module + ".png").convert("RGBA")
        except IOError:
            continue
        for x in range(864):
            for y in range(864):
                pixel = image.getpixel((x, y))
                if pixel != (255, 255, 255, 0):
                    im.putpixel((x, y), image.getpixel((x, y)))
    response = HttpResponse(content_type="image/png")
    im.save(response, "PNG")
    return response


urlpatterns = [
    url(r'^.*$', diagram)
]
