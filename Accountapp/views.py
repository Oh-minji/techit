from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import base
from django.urls import reverse

from Accountapp.models import Registration


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        email = request.POST.get('Email')

        reg = Registration()
        reg.email = email
        reg.save()


        return HttpResponseRedirect(reverse("accountapp:hello_world"))

    reg_all = Registration.objects.all()

    temp = "stellup"
    return render(request, "accountapp/Hello_World.html",
                  context = {"temp": temp,
                             "reg_all" : reg_all})