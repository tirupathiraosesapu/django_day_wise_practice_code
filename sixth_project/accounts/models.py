from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # db_table = "employees"
        ordering = ['employee_name']
        verbose_name = "employee"
        verbose_name_plural = "Employees Details"


class Role(models.Model):
    role_name = models.CharField(max_length=30)