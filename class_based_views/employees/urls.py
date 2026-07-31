from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    # path("class/", views.ClassBasedView.as_view(), name="class"),
    # path("get_all_employees/", views.GetAllEmployees.as_view(), name="get_all_employees"),
    # path("all_employees/", views.EmployeeList.as_view(), name="all_employees"),
    # path("view_employees/", views.EmployeeListView.as_view(), name="view_employees"),
    path("department/<str:role>/", views.EmployeeDepartmentListView.as_view(), name="department_employees"),
    path("", views.EmployeesFullList.as_view(), name="employee_list"),
    path("employees/<int:pk>/", views.EmployeeDetailedView.as_view(), name="employee_detail")
]