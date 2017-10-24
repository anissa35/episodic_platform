from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'author_platform/home.html')
