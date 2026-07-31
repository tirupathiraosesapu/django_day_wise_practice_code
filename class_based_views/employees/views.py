from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Employee

# Function based views
def home(request):
    context = {"title": "Class Based View", "SessionNo": 22}
    return render(request, "index.html", context)

# Class Based VIew
class ClassBasedView(View):
    def get(self, request):
        context = {"title": "Class Based View", "SessionNo": 22}
        return render(request, "dashboard.html", context)

    def post(self, request):
        return render(request, "home.html")

class GetAllEmployees(View):
    def get(self, request):
        employee = Employee.objects.all()
        return render(request, "employee_list.html", {"employees":employee})

# generic class based view
class EmployeeList(ListView):
    model = Employee
    # queryset = Employee.objects.all()
    queryset = Employee.objects.filter(role="manager")
    context_object_name = "employees"
    template_name = ("employee_list.html")

class EmployeeListView(ListView):
    model = Employee
    context_object_name = "employees"
    # ordering = ["-department"]
    template_name = ("employee_list.html")

    # def get_queryset(self):
    #     return Employee.objects.filter(status="inactive")

    def get_queryset(self):
        queryset = Employee.objects.all()
        search = self.request.GET.get("search")
        status = self.request.GET.get("status")

        if search:
            queryset = Employee.objects.filter(department__icontains= search)
        if status:
            queryset = Employee.objects.filter(status = status)

        return queryset

class EmployeeDepartmentListView(ListView):
    model = Employee
    context_object_name = "employees"
    template_name = ("employee_list.html")

    def get_queryset(self):
        department = self.kwargs["role"]
        return Employee.objects.filter(role=department)

class EmployeesFullList(ListView):
    model = Employee
    context_object_name = "employees"
    # queryset = Employee.objects.all()
    template_name = ("employee_list.html")
    ordering = ["first_name"]
    paginate_by = 20

    def get_queryset(self):
        queryset = Employee.objects.all()
        search = self.request.GET.get("search")
        status = self.request.GET.get("status")
        if search:
            queryset = Employee.objects.filter(
                Q(first_name__icontains=search)                 
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
                | Q(department__icontains=search)
                | Q(designation__icontains=search)

            )
        if status:
            queryset = Employee.objects.filter(status=status)
        return queryset

class EmployeeDetailedView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = ("employee_details.html")

    def get_object(self):
        # employee_id = self.kwargs["pk"]
        employee_id = self.kwargs.get("pk")
        employee = Employee.objects.get(pk=employee_id)
        return employee