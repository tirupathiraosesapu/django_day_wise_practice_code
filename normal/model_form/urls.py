from django.urls import path
from .views import *

urlpatterns = [
    path("", register_employee, name="register"),
]