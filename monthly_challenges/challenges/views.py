from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("work 9 hours every day!")


def february(request):
    return HttpResponse("run 45 mins every day!")
