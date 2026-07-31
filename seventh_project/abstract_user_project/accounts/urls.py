from django.urls import path
from .views import *

urlpatterns = [
    path("registration/", registration_view, name="registration"),
    path("login/", login_view, name="login"),
    path("", dashboard_view, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("test/", send_test_mail, name="test-mail"),
    path("verify-otp/<int:id>/", verify_registerd_otp, name="verify-otp"),
    path("resend-otp/<int:id>/", resend_otp, name="resend-otp"),
    path("change-password/", change_password, name="change-password"),
    path("forgot-password/",forgot_password, name="forgot-password"),
    path("reset-password/<uid>/<token>/", reset_password, name="reset-password")

]
