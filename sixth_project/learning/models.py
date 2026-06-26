from django.db import models

# Create your models here.
class Batch(models.Model):
    batch_name = models.CharField(max_length=30)