from django.shortcuts import render
from .models import TbAdmin

# Create your views here.

def home(request):
    return render(request, "home.html")

def startapps(request):
    return render(request, "app/start.html")

def loginapp(request):
    result = TbAdmin.objects.all()
    data = {
        'result': result
    }
    return render(request, "app/login.html", data)