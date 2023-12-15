from . import date time
rom django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "newyear/index.html")