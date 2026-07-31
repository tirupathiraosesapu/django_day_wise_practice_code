from django import forms
from .models import Employee

DEPARTMENT_CHOICES = (
        ("Python", "Python"),
        ("Java", "Java"),
        ("Testing", "Testing"),
        ("HR", "HR"),
        ("React", "React"),
    )

CITY_CHOICES = (
    ("Hyderabad", "Hyderabad"),
    ("Bangalore", "Bangalore"),
    ("Chennai", "Chennai"),
    ("Vijayawada", "Vijayawada"),
)
class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=10)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    salary = forms.DecimalField()
    city = forms.ChoiceField(choices=CITY_CHOICES)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) <3:
            raise forms.ValidationError("Name should be atleast above 3 characters")
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only alphabets."
            )
        return name
    
    def clean_email(self):
        email = self.cleaned_data["email"]

        if Employee.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email Already existed"
            )
        return email
    
    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        if not mobile.isdigit():
            raise forms.ValidationError(
            "Mobile should contain only numbers."
            )
        if len(mobile) != 10:
            raise forms.ValidationError(
            "Mobile number should contain exactly 10 digits."
            )
        if Employee.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError(
            "Mobile number already exists."
            )
        return mobile
    
    def clean_department(self):
        department = self.cleaned_data["department"]
        if department == "":
            raise forms.ValidationError(
                "Please select department."
            )
        return department
    
    def clean_salary(self):
        salary = self.cleaned_data["salary"]
        if salary < 10000:
            raise forms.ValidationError(
                "Minimum salary should be 10000."
            )
        if salary > 500000:
            raise forms.ValidationError(
                "Maximum salary should be 500000."
            )
        return salary
    
    def clean_city(self):
        city = self.cleaned_data["city"]
        if city == "":
            raise forms.ValidationError(
                "Please select city."
            )
        return city
    
    def clean(self):
        cleaned_data =super().clean()
        department = cleaned_data.get("department")
        salary = cleaned_data.get("salary")

        if department == "HR" and salary <30000:
            raise forms.ValidationError(
                "HR Department salary should be greater than 30000"
            )
        return cleaned_data






