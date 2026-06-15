from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return HttpResponse("This is my welcome page from django")

def Register(request):
    return HttpResponse("<h1>This is from register page</h1>")
