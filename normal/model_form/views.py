from django.shortcuts import render
from .forms import EmployeeForm


def register_employee(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return render(request,"register.html", { "form": EmployeeForm(), "success": "Employee Registered Successfully",} )

            except Exception as e:

                return render(request, "register.html", {"form": form, "db_error": str(e)} )
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = EmployeeForm()
    return render(request, "register.html", {"form": form})
