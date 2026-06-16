from django.urls import path
from .views import home, aboutUs, contactUs, leaves, employee

urlpatterns = [
    path("", home),
    path("about-us/", aboutUs),
    path("contact-us/", contactUs),
    path("leaves/", leaves),
    path("employee/", employee),
    # path("welcome/", welcomeHome)
]
