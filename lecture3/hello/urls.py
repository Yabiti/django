from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("yabu", views.yabu, name="yabu"),
    path('David', views.David, name="David"),
]
