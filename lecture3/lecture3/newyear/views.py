import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    datetime = datetime.datetimenow()
    return render(request, "newyear/index.html")