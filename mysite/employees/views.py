from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse('hi')
# Create your views here.
