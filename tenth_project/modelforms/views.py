from django.shortcuts import render
from .forms import EmployeeModelForm


# Create your views here.
def registration_view_model_form(request):
    if request.method == "GET":
        form = EmployeeModelForm()
        return render(request, "registration.html", {"form": form})

    if request.method == "POST":
        form = EmployeeModelForm(request.POST)

        if form.is_valid():
            try:
                employee = form.save(commit=False)
                print(employee)
                employee.is_active = False
                employee.email = employee.email.lower()
                employee.name = employee.name.upper()
                employee.save()
                return render(
                    request,
                    "registration.html",
                    {
                        "form": EmployeeModelForm(),
                        "success": "User registration successfull from the Modelforms",
                    },
                )
            except Exception as e:
                print(e)
                return render(
                    request,
                    "registration.html",
                    {"form": EmployeeModelForm(), "db_error": str(e)},
                )
        else:
            return render(request, "registration.html", {"form": form})            
