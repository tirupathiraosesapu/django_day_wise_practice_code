from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    clean_is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.username
