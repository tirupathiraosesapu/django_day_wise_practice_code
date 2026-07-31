from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee

        fields = ["name", "email", "mobile", "department", "salary", "city"]

    # -----------------------------
    # Name Validation
    # -----------------------------
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Name must contain at least 3 characters.")

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name should contain only alphabets.")

        return name

    # -----------------------------
    # Email Validation
    # -----------------------------
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Employee.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return email

    # -----------------------------
    # Mobile Validation
    # -----------------------------
    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must contain exactly 10 digits.")

        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")

        if Employee.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("Mobile number already exists.")

        return mobile

    # -----------------------------
    # Salary Validation
    # -----------------------------
    def clean_salary(self):
        salary = self.cleaned_data.get("salary")
        if salary < 10000:
            raise forms.ValidationError("Minimum salary should be 10,000.")

        if salary > 300000:
            raise forms.ValidationError("Salary cannot exceed 3,00,000.")

        return salary

    # -----------------------------
    # Department Validation
    # -----------------------------
    def clean_department(self):
        department = self.cleaned_data.get("department")
        allowed_departments = ["HR", "IT", "Finance", "Sales", "Marketing"]
        if department not in allowed_departments:
            raise forms.ValidationError("Please choose a valid department.")

        return department

    # -----------------------------
    # City Validation
    # -----------------------------
    def clean_city(self):
        city = self.cleaned_data.get("city")
        if len(city) < 3:
            raise forms.ValidationError("City name is too short.")

        return city

    # -----------------------------
    # Form Level Validation
    # -----------------------------
    def clean(self):
        cleaned_data = super().clean()
        department = cleaned_data.get("department")
        salary = cleaned_data.get("salary")
        if department == "HR" and salary:
            if salary > 100000:
                raise forms.ValidationError(
                    "HR employees cannot have salary greater than 1,00,000."
                )

        return cleaned_data
