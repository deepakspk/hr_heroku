from .models import Department, Employee, Payslip, Additionalpay, Deduction, Timesheet
from django.forms import ModelForm, Form
from django import forms
from . import models

class EmployeeForm(ModelForm):
    class Meta:
        model= Employee
        fields = '__all__'
        exclude = ('employee_status',)
        unique_together = [("first_name", "last_name" )]
        widgets = {
            'DOB':forms.DateInput(attrs={'type':'date'}),
            'joining_date':forms.DateInput(attrs={'type':'date'})
        }

    # def __init__(self, *args, **kwargs):
    #      super().__init__(*args, **kwargs)
    #      for field in self.fields:
    #          self.fields[field].widget.attrs.update({'class':'form-control'})