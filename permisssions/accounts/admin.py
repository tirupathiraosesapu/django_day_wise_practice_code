from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_code",
        "first_name",
        "department",
        "designation",
        "role",
        "status",
    )
    search_fields = ("employee_code", "first_name", "email")
    list_filter = ("department", "role", "status")
