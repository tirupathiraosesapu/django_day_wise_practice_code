from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User, Permission
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy

from .forms import LoginForm, EmployeeForm
from .models import Employee
from .decorators import (
    admin_required,
    manager_required,
    employee_required,
    role_and_permission_required,
)


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")


def create_roles(request):
    Group.objects.get_or_create(name="Admin")
    Group.objects.get_or_create(name="Manager")
    Group.objects.get_or_create(name="Employee")
    return redirect("login")


def create_users(request):
    admin_user, created = User.objects.get_or_create(username="Tirupathi")
    print(admin_user, created)

    if created:
        admin_user.set_password("tirupathi123")
        admin_user.save()

    manager_user, created = User.objects.get_or_create(username="Surya")
    if created:
        manager_user.set_password("surya123")
        manager_user.save()

    employee_user, created = User.objects.get_or_create(username="Manisha")
    if created:
        employee_user.set_password("manisha123")
        employee_user.save()

    print(admin_user, manager_user, employee_user)

    return redirect("login")


def assign_roles(request):
    admin_group = Group.objects.get(name="Admin")
    manager_group = Group.objects.get(name="Manager")
    employee_group = Group.objects.get(name="Employee")

    admin_user = User.objects.get(username="Tirupathi")
    manager_user = User.objects.get(username="Surya")
    employee_user = User.objects.get(username="Manisha")

    admin_user.groups.set([admin_group])
    manager_user.groups.set([manager_group])
    employee_user.groups.set([employee_group])

    print("Roles assignment successfull")

    return redirect("login")


@login_required
def dashboard(request):
    user = request.user
    if user.groups.filter(name="Admin").exists():
        return redirect("admin_dashboard")
    elif user.groups.filter(name="Manager").exists():
        return redirect("manager_dashboard")
    elif user.groups.filter(name="Employee").exists():
        return redirect("employee_dashboard")
    return redirect("unauthorized")


@admin_required
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")


@manager_required
def manager_dashboard(request):
    return render(request, "accounts/manager_dashboard.html")


@employee_required
def employee_dashboard(request):
    return render(request, "accounts/employee_dashboard.html")


def unauthorized(request):
    return render(request, "accounts/unauthorized.html")


def assign_permission(request):
    admin_group = Group.objects.get(name="Admin")
    manager_group = Group.objects.get(name="Manager")
    employee_group = Group.objects.get(name="Employee")

    add_employee = Permission.objects.get(codename="add_employee")
    change_employee = Permission.objects.get(codename="change_employee")
    delete_employee = Permission.objects.get(codename="delete_employee")
    view_employee = Permission.objects.get(codename="view_employee")
    approve_salary = Permission.objects.get(codename="approve_salary")
    approve_leave = Permission.objects.get(codename="approve_leave")

    admin_group.permissions.set(
        [
            add_employee,
            change_employee,
            delete_employee,
            view_employee,
            approve_leave,
            approve_salary,
        ]
    )
    manager_group.permissions.set([view_employee, change_employee, approve_leave])
    employee_group.permissions.set([view_employee])

    return redirect("login")


@login_required
@permission_required("accounts.add_employee", raise_exception=True)
def add_employee(request):
    return render(request, "accounts/add_employee.html")


@login_required
@permission_required("accounts.view_employee", raise_exception=True)
def employee_list(request):
    return render(request, "accounts/employee_list.html")


@login_required
@permission_required("accounts.change_employee", raise_exception=True)
def update_employee(request):
    return render(request, "accounts/update_employee.html")


@login_required
@permission_required("employees.delete_employee", raise_exception=True)
def delete_employee(request):
    return render(request, "accounts/delete_employee.html")


# @login_required
# @permission_required("employees.approve_leave",raise_exception=True)
@role_and_permission_required(["Admin", "Manager"], "accounts.view_employee")
def approve_leave(request):
    return render(request, "accounts/approve_leave.html")


class EmployeesFullList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Employee
    context_object_name = "employees"
    permission_required = "accounts.view_employee"
    # queryset = Employee.objects.all()
    template_name = "accounts/employee_list.html"
    ordering = ["first_name"]
    # paginate_by = 20

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


class EmployeeDetailedView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    model = Employee
    context_object_name = "employee"
    permission_required = "accounts.view_employee"
    template_name = "accounts/employee_details.html"

    def get_object(self):
        # employee_id = self.kwargs["pk"]
        employee_id = self.kwargs.get("pk")
        employee = Employee.objects.get(pk=employee_id)
        return employee


class EmployeeCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "accounts/add_employee.html"
    permission_required = "accounts.add_employee"
    # success_url = reverse_lazy("employee_list")

    def form_invalid(self, form):
        print("Your form is invalid")
        return super().form_invalid(form)

    def form_valid(self, form):
        print("Your form is successfully submitted")
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.groups.filter(name="Admin").exists():
            return reverse_lazy("admin_dashboard")
        elif self.request.user.groups.filter(name="Manager").exists():
            return reverse_lazy("manager_dashboard")
        return reverse_lazy("employee_list")


class EmployeeUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    permission_required = "accounts.change_employee"
    template_name = "accounts/update_employee.html"

    # success_url = reverse_lazy("employee_list")
    def form_valid(self, form):
        employee = form.save()
        messages.success(self.request, f"{employee.first_name} updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors.")
        return super().form_invalid(form)

    def get_success_url(self):
        if self.request.user.groups.filter(name="Admin").exists():
            return reverse_lazy("admin_dashboard")
        elif self.request.user.groups.filter(name="Manager").exists():
            return reverse_lazy("manager_dashboard")
        return reverse_lazy("employee_list")


class EmployeeDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = "accounts/delete_employee.html"
    permission_required = "accounts.delete_employee"
    # success_url = reverse_lazy("employee_list")

    def form_valid(self, form):
        employee_name = self.object.first_name
        print("Form is valid")
        messages.success(self.request, f"{employee_name} deleted successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        messages.error(self.request, "Please correct the errors.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        print("Redirected successfullly")
        if self.request.user.groups.filter(name="Admin").exists():
            return reverse_lazy("admin_dashboard")
        elif self.request.user.groups.filter(name="Manager").exists():
            return reverse_lazy("manager_dashboard")
        return reverse_lazy("employee_list")
