from django.urls import path
from .views import *

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create-roles/", create_roles, name="create_roles"),
    path("create-users/", create_users, name="create_users"),
    path("assign-roles/", assign_roles, name="assign_roles"),
    path("assign-permissions/", assign_permission, name="assign_permission"),
    path("dashboard/", dashboard, name="dashboard"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("manager-dashboard/", manager_dashboard, name="manager_dashboard"),
    path("employee-dashboard/", employee_dashboard, name="employee_dashboard"),
    path("unauthorized/", unauthorized, name="unauthorized"),
    path("add-employee/", EmployeeCreateView.as_view(), name="add_employee"),
    path("employees/", EmployeesFullList.as_view(), name="employee_list"),
    path("update-employee/", update_employee, name="update_employee"),
    path("delete-employee/", delete_employee, name="delete_employee"),
    path("approve-leave/", approve_leave, name="approve_leave"),
    path("employees/<int:pk>/", EmployeeDetailedView.as_view(), name="employee_detail"),
    path("update/<int:pk>", EmployeeUpdateView.as_view(), name="update_employees"),
    path("delete/<int:pk>", EmployeeDeleteView.as_view(), name="delete_employees")
]
