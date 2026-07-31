from django.shortcuts import render
from .models import Employee
from django.db.models import Max, Min, Avg, Count, Sum

# Create your views here.
def HomePage(request):
    employee_list = Employee.objects.all()
    # select * from employee
    
    single_employee = Employee.objects.get(employee_code__iexact="emp0093")
    # select * from employee where employee_code ="Emp0093"
    
    hr_executive = Employee.objects.filter(designation__in=["HR Executive", "Intern"])
    # select * from employee where designation ="HR Executive"

    without_hr_executive = Employee.objects.exclude(designation="HR Executive")
    first_employee_details = Employee.objects.first()

    last_employee_details = Employee.objects.last()

    employee_total_count = Employee.objects.count()

    email_exists = Employee.objects.filter(email="emploee93@gmail.com").exists()

    designation_by_order = Employee.objects.order_by("-designation")

    first_values = Employee.objects.values("first_name", "last_name")

    first_list = Employee.objects.values_list("first_name", "last_name")
    
    departments = Employee.objects.values("department").distinct().order_by("-department")

    total_salary_of_employees = Employee.objects.aggregate(Sum("salary"))

    number_of_total_employees = Employee.objects.aggregate(Count("id"))

    minimum_salary = Employee.objects.aggregate(Min("salary"))
    maximum_salary = Employee.objects.aggregate(Max("salary"))
    average_salary = Employee.objects.aggregate(Avg("salary"))


    # select count(*) from employee

    print(minimum_salary, maximum_salary, average_salary)
    return render(
        request,
        "index.html",
        {
            "employee_list": employee_list,
            "single_employee": single_employee,
            "hr_executive": hr_executive,
            "first_employee_details":first_employee_details,
            "last_employee_details":last_employee_details,
            "without_hr_executive":without_hr_executive,
            "employee_total_count":employee_total_count,
            "email_exists":email_exists,
            "designation_by_order":designation_by_order,
            "first_values":first_values,
            "first_list":first_list,
            "departments":departments,
            "total_salary_of_employees":total_salary_of_employees,
            "number_of_total_employees":number_of_total_employees,
            "minimum_salary":minimum_salary,
            "maximum_salary":maximum_salary,
            "average_salary":average_salary
        },
    )
