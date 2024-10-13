# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')