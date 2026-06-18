from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=50)

    class Meta:
        db_table = "departments"

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Employees'


class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    address = models.TextField()
    profile_picture = models.CharField(max_length=200)

    class Meta:
        db_table = "employee_profile"


class PublicAddress(models.Model):
    employee_profile = models.OneToOneField(EmployeeProfile, on_delete=models.CASCADE)
    door_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=50)

    class Meta:
        db_table = "public_address"

    
class Projects(models.Model):
    project_name = models.CharField(max_length=100)

    class Meta:
        db_table = "projects"

class newEmployee(models.Model):
    employee_name = models.CharField(max_length=50)
    project = models.ManyToManyField(Projects)

    class Meta:
        db_table = "new_employees"