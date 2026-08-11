from django.urls import path

from .views import (RegisteredAPIView, LoginAPIView, LogoutAPIView, csrf_token_view)

urlpatterns = [
    path("csrf/", csrf_token_view, name="csrf"),
    path("register/", RegisteredAPIView.as_view(), name="register_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("logout/", LogoutAPIView.as_view(), name="logout_api"),
]
