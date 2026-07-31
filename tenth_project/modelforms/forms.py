from django import forms
from .models import Employee


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            "name": "Employee Name",
            "email": "Employee Email",
            "mobile": "Mobile Number",
            "gender": "Gender",
            "department": "Department",
            "salary": "Salary",
            "city": "City",
            "joining_date": "Joining Date",
            "is_active": "Employee Active Status",
        }
        help_texts = {
            "salary": "Minimum salary should be ₹10,000.",
            "mobile": "Enter exactly 10 digits.",
            "joining_date": "Select employee joining date.",
        }
        error_messages = {
            "name": {"required": "Employee name is required."},
            "email": {
                "required": "Email is mandatory.",
                "invalid": "Enter a valid email address.",
            },
            "mobile": {"required": "Mobile number is required."},
        }
        widgets = {
             "name": forms.TextInput(
                attrs={
                    "id":"python with django",
                    "class": "tirupathi",
                    "placeholder": "Enter Employee Name"
                }
            ),
             "email": forms.EmailInput(
                attrs={
                    "class": "charan",
                    "placeholder": "Enter Email"
                }
            ),
            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Mobile Number"
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "department": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "salary": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Salary"
                }
            ),
            "city": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "joining_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            )
        }

