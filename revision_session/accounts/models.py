from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'employees'
        ordering = ['employee_name']
        verbose_name = "Employee"
        verbose_name_plural = "Emp"
    
    def __str__(self):
        return self.employee_name

class EmployeeProfiel(models.Model):
    door_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=100)
    employee_id = models.OneToOneField(Employees, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee_profile"