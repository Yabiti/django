from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
    path("yabiti", views.yabiti, name="yabiti")
]