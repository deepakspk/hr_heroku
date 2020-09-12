from .models import Department, Employee, Payslip, ProcessSalary, Additionalpay, Deduction, Timesheet, Clinical, WorkPermit, LaborContract, EidCollect, NewEid
from django.forms import ModelForm, Form
from django import forms
from . import models

class DepartmentForm(ModelForm):
    class Meta:
        model= Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class EmployeeForm(ModelForm):
    class Meta:
        model= Employee
        fields = '__all__'
        # exclude = ('employee_status',)
        unique_together = [("first_name", "last_name" )]
        widgets = {
            'DOB':forms.DateInput(attrs={'type':'date'}),
            'joining_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class AdditionalForm(ModelForm):
    class Meta:
        model= Additionalpay
        fields = '__all__'
        widgets = {
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'})
        }


    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class DeductionForm(ModelForm):
    class Meta:
        model= Deduction
        fields = '__all__'
        widgets = {
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class TimesheetForm(ModelForm):
    class Meta:
        model= Timesheet
        fields = '__all__'
        widgets = {
            'month':forms.DateInput(attrs={'type':'date'}),
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})



class PayslipForm(ModelForm):
    class Meta:
        model= Payslip
        fields = '__all__'
        widgets = {
            'joining_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         data = models.Payslip.objects.all().values_list('employee',flat=True)
         # self.fields['employee'].queryset = models.Employee.objects.exclude(employee_id__in=data)
         self.fields['employee'].queryset = models.Employee.objects.exclude(employee_status = 'Inactive')
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})


class ProcessSalaryForm(ModelForm):
    class Meta:
        model= ProcessSalary
        fields = '__all__'
        exclude = ('status','gross_pay','Additional_pay','deduction','total', 'employee_count', 'actual_gross_pay')
        widgets = {
            'salary_month':forms.DateInput(attrs={'type':'date'}),
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'finish_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class LabourContractForm(ModelForm):
    class Meta:
        model= LaborContract

        
        fields = '__all__'
        widgets = {
            'contract_issue_date':forms.DateInput(attrs={'type':'date'}),
            'contract_collected_date':forms.DateInput(attrs={'type':'date'}),
            'passport_collect_date':forms.DateInput(attrs={'type':'date'}),
            'medical_date':forms.DateInput(attrs={'type':'date'}),
            'passport_receive_date':forms.DateInput(attrs={'type':'date'}),
            'passport_returned_date':forms.DateInput(attrs={'type':'date'})
           }
            

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['employee'].queryset = models.Employee.objects.exclude(employee_status = 'Exiting')
         for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class WorkPermitForm(ModelForm):
    class Meta:
        model= WorkPermit
        fields = '__all__'
        widgets = {
            'contract_issue_date':forms.DateInput(attrs={'type':'date'}),
            'contract_collected_date':forms.DateInput(attrs={'type':'date'}),            
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class EidCollectForm(ModelForm):
    class Meta:
        model= EidCollect
        fields = '__all__'
        widgets = {
            'eid_requested_date':forms.DateInput(attrs={'type':'date'}),
            'eid_collected_date':forms.DateInput(attrs={'type':'date'}),
            'eid_returned_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class NewEidForm(ModelForm):
    class Meta:
        model= NewEid
        fields = '__all__'
        widgets = {
            'eid_received_date':forms.DateInput(attrs={'type':'date'}),
            'eid_collected_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})


class PassportReturnUpdateForm(ModelForm):
    class Meta:
        model= LaborContract
        fields = '__all__'
        exclude = ('contract_issue_date','contract_collected_date','passport_collect_date','medical_done','medical_date','contract_collected','passport_collected',)
        widgets = {
            'contract_issue_date':forms.DateInput(attrs={'type':'date'}),
            'contract_collected_date':forms.DateInput(attrs={'type':'date'}),
            'passport_collect_date':forms.DateInput(attrs={'type':'date'}),
            'medical_date':forms.DateInput(attrs={'type':'date'}),
            'passport_receive_date':forms.DateInput(attrs={'type':'date'}),
            'passport_returned_date':forms.DateInput(attrs={'type':'date'})
           }
            

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})