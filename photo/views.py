from django.shortcuts import render
from .tasks import download_photo
from . import tasks


def index(request):
    tasks.download_photo.delay()
    return render(request, "photo/index.html")
