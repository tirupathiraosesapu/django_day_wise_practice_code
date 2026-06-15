from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse("This is my dashabord page")


def welcomeHome(request):
    homeData = {"name": "tirupathi rao sesapu", "age": 28, "fullName": "Hyderabad"}
    # homeData = ["Manisha", "Surya", "Charan", "Tirupathi", "Harshik", "Harish"]
    # homeData = {"is_active": True}
    # return render(request, "home.html", {"homeData": homeData})
    return render(request, "home.html", homeData)
