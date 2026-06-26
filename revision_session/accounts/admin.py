from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = [
        'employee_name', 'salary', 'email'
    ]
    search_fields = [
        'email', 'employee_name'
    ]
    list_filter = [
        'email'
    ]

admin.site.register(EmployeeProfiel)