from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("super_admin", "Super Admin"),
    ("admin", "Admin"),
    ("manager", "Manager"),
    ("employee", "Employee"),
    ("user", "User"),
)


# Create your models here.
class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "abstract_user"

    def __str__(self):
        return self.username
