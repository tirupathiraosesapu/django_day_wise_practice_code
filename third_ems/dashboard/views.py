from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse("This is my dashabord page")


"""def welcomeHome(request):
    homeData = {"name": "tirupathi rao sesapu", "age": 28, "fullName": "Hyderabad"}
    # homeData = ["Manisha", "Surya", "Charan", "Tirupathi", "Harshik", "Harish"]
    # homeData = {"is_active": True}
    # return render(request, "home.html", {"homeData": homeData})
    return render(request, "home.html", homeData)"""


def home(requset):
    return render(requset, "dashboard.html")


def aboutUs(requset):
    return render(requset, "aboutus.html")


def contactUs(requset):
    return render(requset, "contactus.html")


def employee(requset):
    return render(requset, "employee.html")


def leaves(requset):
    return render(requset, "leaves.html")
