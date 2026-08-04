from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .models import Employee


@receiver(pre_save, sender=Employee)
def employee_pre_save(sender, instance, **kwargs):
    print("Before Saving Employee")
    instance.first_name = instance.first_name.title()
    # instance.last_name = instance.last_name.title()

@receiver(post_save, sender=Employee)
def employee_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Welcome {instance.first_name}")
    else:
        print(f"{instance.first_name} Updated Successfully")

@receiver(post_delete, sender=Employee)
def employee_post_delete(sender, instance, **kwargs):
    print(f"{instance.first_name} Deleted Successfully")
