from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def index(request):
    workers = Worker.objects.all()
    return render(request, 'employees/index.html', {'worcers': workers, 'title': 'Главная страница'})
# Create your views here.
