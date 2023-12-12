from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(rewuest):
    return HttpResponse("Hello, World!")
