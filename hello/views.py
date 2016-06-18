from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pacotes(request):
    return render(request, 'pacotes.html')

def london_design(request):
    return render(request, 'london_design.html')

def parceiros(request):
    return render(request, 'parceiros.html')
