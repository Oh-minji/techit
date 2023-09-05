from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import base
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

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

class AccountCreateView(CreateView):
        model = User
        form_class = UserCreationForm
        success_url = reverse_lazy("accountapp:hello_world")
        template_name = "accountapp/create.html"

class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"

class AccountLogoutView(LogoutView):
    pass

class AccountDetailView(DetailView):
    model = User
    template_name = "accountapp/detail.html"
    context_object_name = "target_user"