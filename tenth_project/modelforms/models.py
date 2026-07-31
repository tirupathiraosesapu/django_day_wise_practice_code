from django.db import models


class Employee(models.Model):
    DEPARTMENT_CHOICES = (
        ("Python", "Python"),
        ("Java", "Java"),
        ("React", "React"),
        ("Testing", "Testing"),
        ("HR", "HR"),
    )
    CITY_CHOICES = (
        ("Hyderabad", "Hyderabad"),
        ("Bangalore", "Bangalore"),
        ("Chennai", "Chennai"),
        ("Vijayawada", "Vijayawada"),
    )
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employee_modelform"
        ordering = ["-created_at"]
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name
