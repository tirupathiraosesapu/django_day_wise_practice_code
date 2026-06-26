from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    # return HttpResponse("<h2>Welcome to the homepage</h2>")
    return render(request, 'index.html')