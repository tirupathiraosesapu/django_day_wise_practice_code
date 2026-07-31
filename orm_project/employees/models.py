from django.db import models


class Employee(models.Model):

    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("Team Lead", "Team Lead"),
        ("Employee", "Employee"),
        ("Intern", "Intern"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Resigned", "Resigned"),
    ]

    employee_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    experience = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    joining_date = models.DateField()
    last_login = models.DateTimeField(null=True, blank=True)
    profile_completed = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employees"

    def __str__(self):
        return f"{self.employee_code} - {self.first_name}"
