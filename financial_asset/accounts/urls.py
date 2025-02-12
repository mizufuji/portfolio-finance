from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.views.generic import CreateView


urlpatterns = [
    path(
        "signup/",
        CreateView.as_view(
            template_name="registration/signup.html",
            form_class=UserCreationForm,
            success_url="/",
        ),
        name="signup",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
