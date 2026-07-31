from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee


def register_employee(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

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
                    {
                        "form": EmployeeForm(),
                        "success": "Employee Registered Successfully",
                    },
                )

            except Exception as e:
                return render(
                    request, "register.html", {"form": form, "db_error": str(e)}
                )

        else:
            return render(request, "register.html", {"form": form})

    else:
        form = EmployeeForm()
    return render(request, "register.html", {"form": form})
