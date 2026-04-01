from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_id': 'Employee ID',
            'name': 'Employee Name',
            'salary': 'Employee Salary',
            'designation': 'Employee Designation',
            'company': 'Employee Company',
            'email_address': 'Employee Email'
        }
