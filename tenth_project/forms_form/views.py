from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def employee_registration(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                Employee.objects.create(
                    name=form.cleaned_data["name"],
                    email=form.cleaned_data["email"],
                    mobile=form.cleaned_data["mobile"],
                    department=form.cleaned_data["department"],
                    salary=form.cleaned_data["salary"],
                    city=form.cleaned_data["city"],
                )
                return render(
                    request,
                    "register.html",
                    {"form": EmployeeForm(), "success": "User registered successfully"},
                )
            except Exception as e:
                print(e)
                return render(
                    request,
                    "register.html",
                    {"form": EmployeeForm(), "db_error": str(e)},
                )
    else:
        form = EmployeeForm()
    return render(request, "register.html", {"form": form, "db_error":""})
