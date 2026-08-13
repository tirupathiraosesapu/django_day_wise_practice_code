from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        EMPLOYEE = "EMPLOYEE", "Employee"
        USER = "USER", "User"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER
    )

    def __str__(self):
        return self.username