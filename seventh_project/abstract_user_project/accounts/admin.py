from django.contrib import admin
from .models import User


# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "mobile_number", "role", "is_verified")

    search_fields = ("email", "username")

    list_filter = ("role", "is_verified")
