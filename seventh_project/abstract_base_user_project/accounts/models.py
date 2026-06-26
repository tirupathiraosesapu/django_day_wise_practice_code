from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.


ROLE_CHOICES = (
    ("super_admin", "Super Admin"),
    ("admin", "Admin"),
    ("manager", "Manager"),
    ("employee", "Employee"),
    ("user", "User"),
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, mobile, password=None, role="user"):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        print(email)
        user = self.model(username=username, mobile=mobile, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        print(user)
        return user

    def create_super_user(self, email, username, mobile, password):
        user = self.create_user(
            email=email,
            username=username,
            mobile=mobile,
            password=password,
            role="super_admin",
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)

        print(user)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(unique=True, max_length=15)
    role = models.CharField(choices=ROLE_CHOICES, default="user", max_length=20)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "mobile"]

    def __str__(self):
        return self.username
