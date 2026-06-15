from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

# Create your views here.


def employeeDashboard(request):
    print(request.method)
    return HttpResponse(
        "<h1>This is from employee dashboard</h1><p>Thi si sthe main page of the employee dashboard</p>"
    )


def employeeDetails(request):
    return HttpResponse("This is the employee single page")


def employeeProfile(request):
    return HttpResponse("This is the employee profile")


def employeeList(request, id):
    return HttpResponse(f"Employee Id : {id}")


def employeeName(request, name):
    # return HttpResponse(f"Employee Name : {name}")
    return redirect("profile/")


def employeeValues(request, id, name):
    print(request.method)
    print(request.user)
    return HttpResponse(f"Employee Name : {name}\nEmployee Id : {id}")


def employeeData(request):
    data = {"id": 12, "name": "Surya", "course": "Python Full Stack"}

    return JsonResponse(data)
