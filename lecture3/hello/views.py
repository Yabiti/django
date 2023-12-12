from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def yabu(request):
    return HttpResponse("Hello, yabu!")

def David(request):
    return HttpResponse("Hello, David")
def greet(requeat, name):
    return HttpResponse(f"hello, {name}.capitalize")