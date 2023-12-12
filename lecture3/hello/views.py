from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def yabu(request):
    return HttpResponse("Hello, yabu!")

def David(request):
    return HttpResponse("Hello, David")
def render(request, "hello/greet.html"):
    return 