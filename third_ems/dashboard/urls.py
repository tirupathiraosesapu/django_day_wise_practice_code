from django.urls import path
from .views import Home, welcomeHome

urlpatterns = [
    path("", Home), 
    path("welcome/", welcomeHome)
]
