from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    employee_code = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    mobile = serializers.CharField(max_length=15)
    department = serializers.CharField(max_length=100)
    designation = serializers.CharField(max_length=100)
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)

class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = "__all__"
        # fields = ["id", "employee_code", "first_name", "email"]
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
        extra_kwargs = {"email": {"required": True}, "salary": {"required": False}}
