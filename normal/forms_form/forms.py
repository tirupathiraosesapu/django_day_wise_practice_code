from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=15)
    department = forms.CharField(max_length=100)
    salary = forms.DecimalField()
    city = forms.CharField(max_length=100)