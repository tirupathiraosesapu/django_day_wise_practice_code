from django.urls import path

from .views import EmployeeAPIView, EmployeeDetailedAPIView, EmployeeGenericAPIView, EmployeeDetailedGenericAPIView, EmployeeListCreateAPIView, EmployeeDetailAPIView

urlpatterns = [
    path("", EmployeeListCreateAPIView.as_view(), name="get_all_employees"),
    path("<int:pk>/", EmployeeDetailAPIView.as_view(), name="get_single_employee_by_id")
]