from django.contrib import admin
# from .models import Employees, Role
from .models import *

# Register your models here.
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'email', 'salary', 'created_at']
    search_fields = ["employee_name", 'email']
    list_filter = ["email"]


admin.site.register(Role)