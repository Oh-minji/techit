from django.urls import path

from Accountapp.views import hello_world, AccountCreateView, AccountLoginView, AccountLogoutView

app_name = "accountapp"


urlpatterns = [
    path("hello_world/", hello_world, name= "hello_world"),

    path("create/", AccountCreateView.as_view(), name = "create" ),

    path("login/", AccountLoginView.as_view(), name = "login"),

    path("logout/", AccountLogoutView.as_view(), name = "logout")
]