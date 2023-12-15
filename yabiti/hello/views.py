from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Say Hello To This World!")
def yabiti(request):
    return HttpResponse("Hello, yabiti!")
def barni(request):
    return HttpResponse("Hello, Barni!")
def greet(request, name):
    return(f"Hello, {name}")