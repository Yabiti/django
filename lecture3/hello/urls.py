from django.urls import path

from . import views

urlspattern = [
    path("", viiews.index, name="index")
]