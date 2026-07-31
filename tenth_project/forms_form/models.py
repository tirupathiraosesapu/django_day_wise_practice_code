from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = (
        ("Python", "Python"),
        ("Java", "Java"),
        ("Testing", "Testing"),
        ("HR", "HR"),
        ("React", "React"),
    )

    CITY_CHOICES = (
        ("Hyderabad", "Hyderabad"),
        ("Bangalore", "Bangalore"),
        ("Chennai", "Chennai"),
        ("Vijayawada", "Vijayawada"),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "employee_forms"

    def __str__(self):
        return self.name
