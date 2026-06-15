from django.urls import path, re_path
from .views import (
    employeeDashboard,
    employeeDetails,
    employeeProfile,
    employeeList,
    employeeName,
    employeeValues,
    employeeData,
)

urlpatterns = [
    path("", employeeDashboard),
    re_path(r"^employee/[0-9]+/$", employeeDetails),
    path("profile/", employeeProfile),
    path("<int:id>", employeeList),
    path("<str:name>", employeeName),
    path("<int:id>/<str:name>", employeeValues),
    path("employee-data/", employeeData),
]
