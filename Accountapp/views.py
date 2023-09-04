from django.http import HttpResponse
from django.shortcuts import render
from django.template import base

from Accountapp.models import Registration


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        email = request.POST.get('Email')

        reg = Registration()
        reg.email = email
        reg.save()

        reg_all = Registration.objects.all()


        return render(request, "accountapp/Hello_World.html",
                      context={"temp": email,
                               "reg_all": reg_all})

    temp = "stellup"
    return render(request, "accountapp/Hello_World.html",
                  context = {"temp": temp})