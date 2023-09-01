from django.http import HttpResponse
from django.shortcuts import render
from django.template import base


# Create your views here.

def hello_world(request):
    return render(request, "accountapp/Hello_World.html")