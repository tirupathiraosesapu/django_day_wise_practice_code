from django.urls import path
from .views import Home, Register

urlpatterns = [path("", Home), path("register/", Register)]
