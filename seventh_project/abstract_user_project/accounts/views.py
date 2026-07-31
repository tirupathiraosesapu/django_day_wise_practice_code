from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from random import randint
from django.contrib.auth import update_session_auth_hash
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from .otp import generate_otp



# Create your views here.
def registration_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # print(email, mobile, username, password)

        if not email or not mobile or not username or not password:
            return render(
                request, "registration.html", {"error": "All fields are mandatory"}
            )

        if User.objects.filter(email=email).exists():
            return render(
                request, "registration.html", {"error": "Email already existed"}
            )

        otp_value = generate_otp()

        user = User.objects.create_user(
            username=username, email=email, mobile_number=mobile, password=password
        )

        user.otp = otp_value
        user.is_verified = False
        user.save()

        send_mail(
            "Employee Management System -- OTP verification",
            f"My name is {username}\nYour OTP is {otp_value}",
            "tirupathiraosesapu@gmail.com",
            [email],
            fail_silently=False,
        )

        # User.objects.create_superuser(
        #     username=username, email=email, mobile_number=mobile, password=password
        # )

        return redirect(f"/verify-otp/{user.id}")

    return render(request, "registration.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return render(request, "dashboard.html")
        else:
            return render(request, "login.html", {"error": "User details not found"})

    return render(request, "login.html")

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html")

def send_test_mail(request):
    send_mail(
        "This is the test connection",
        "This is comes from the django application",
        "tirupathiraosesapu@gmail.com",
        ["tirupathistr@gmail.com"],
        fail_silently=False,
    )

    return HttpResponse("Mail sent successfully")

def verify_registerd_otp(request, id):
    user = User.objects.get(id=id)
    # print(request)
    # print(request.POST.get("reg-otp"))

    # print(user)
    if request.method == "POST":
        otp_verification_value = request.POST.get("reg-otp")
        # print(otp_verification_value)
        # print(user)
        if str(user.otp) == str(otp_verification_value):
            user.is_verified = True
            user.is_active = True
            user.otp = None
            user.save()

            return render(request, "login.html")
        # else:
        #     return render(request, "verify_reg_otp.html", {"error": "Invalid OTP", "user":user})

    return render(request, "verify_reg_otp.html", {"user":user})

def resend_otp(request, id):
    user = User.objects.get(id=id)

    new_otp = generate_otp()
    user.otp = new_otp
    user.save()

    send_mail(
            "Employee Management System -- Resend OTP verification",
            f"My name is {user.username}\nYour OTP is {new_otp}",
            "tirupathiraosesapu@gmail.com",
            [user.email],
            fail_silently=False,
        )

    return render(request, "verify_reg_otp.html", {"user":user})

@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user

        if not user.check_password(old_password):
            return render(request, "change_password.html", {"error": "Old password is not matched"})
        
        if new_password !=confirm_password:
            return render(request, "change_password.html", {"error": "Cnfm password is not matched"})
        
        if len(confirm_password) <8:
            return render(request, "change_password.html", {"error": "Password length must be 8 charactesr"})
        
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)


    return render(request, "change_password.html")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = User.objects.get(email=email)
        except:
            return render(request, "forget_password.html", {"error":"Email is not valid"})
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("User PK",user.pk)
        print("Force Bytes",force_bytes(user.pk))
        print("UID",uid)
        token = default_token_generator.make_token(user)
        print("Token :",token)

        reset_link = f"http://127.0.0.1:8000/reset-password/{uid}/{token}"

        send_mail(
            "Employee Management System -- Forgot password verification",
            f"My name is {user.username}\nYour Reset password link {reset_link}",
            "tirupathiraosesapu@gmail.com",
            [user.email],
            fail_silently=False,
        )
        
        return render(request, "forget_password.html", {"success":"Password reset link is sent"})

    return render(request, "forget_password.html")

def reset_password(request, uid, token):
    uid = urlsafe_base64_decode(uid).decode()
    user = User.objects.get(pk=uid)

    if not default_token_generator.check_token(user, token):
        return render(request, "reset_password.html", {"error":"Invalid token"})
    
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password !=confirm_password:
            return render(request, "change_password.html", {"error": "Cnfm password is not matched"})
        
        if len(confirm_password) <8:
            return render(request, "change_password.html", {"error": "Password length must be 8 charactesr"})
        
        user.set_password(new_password)
        user.save()

        return redirect("login")

    return render(request, "reset_password.html")