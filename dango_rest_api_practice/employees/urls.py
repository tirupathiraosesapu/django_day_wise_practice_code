from django.urls import path

from .views import EmployeeAPIView, EmployeeDetailedAPIView

urlpatterns = [
    path("", EmployeeAPIView.as_view(), name="get_all_employees"),
    path("<int:employee_id>/", EmployeeDetailedAPIView.as_view(), name="get_single_employee_by_id")
]