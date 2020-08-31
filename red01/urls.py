from django.urls import path
from red01 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
]
