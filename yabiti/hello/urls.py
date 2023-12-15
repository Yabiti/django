from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("yabiti", views.yabiti, name="yabiti"),
    path("barni", views.barni, name="barni")
]