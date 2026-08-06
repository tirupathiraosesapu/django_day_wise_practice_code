from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 5 * 1024 * 1024

    if file.size > max_size:
        raise ValidationError("File must be below 5 MB")

class Employee(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("Employee", "Employee"),
    ]
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]
    employee_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Employee")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True, 
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]), validate_file_size
        ]
    )
    resume = models.FileField(upload_to="resumes/", blank=True, null=True, 
        validators=[
                    FileExtensionValidator(allowed_extensions=["docx", "pdf", "xlsx", "doc"]), validate_file_size
            ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employees"
        permissions = [
            ("approve_leave", "Can Approve Leave"),
            ("approve_salary", "Can Approve Salary"),
        ]

    def __str__(self):
        return f"{self.employee_code} - {self.first_name}"
