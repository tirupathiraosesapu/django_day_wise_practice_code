from django.http import HttpResponse

def Home(request):
    return HttpResponse("This is my accounts dashboard page")
