from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (View, ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView)
from . import models
from . forms import EmployeeForm
import re, os
from datetime import date
from django.db.models import Sum, Avg, Max, Count, Min
from django.db.models.functions import Coalesce
from django.db.models import Value
from openpyxl import Workbook
from openpyxl.styles import colors, Color, Border, Side, PatternFill, Font, GradientFill, Alignment
from os import path
from django.http import HttpResponse
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin, TemplateResponseMixin
from easy_pdf.rendering import render_to_pdf_response
from django.contrib import messages
import csv, io
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import FileResponse
from django.http import Http404
from django.views.generic.detail import BaseDetailView
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Create your views here.

def IndexView(request):
    return render(request, 'userapp/index.html')

def ProfileView(request):
    emp = models.Employee.objects.get(email=request.user.email)
    payslip = models.Payslip.objects.get(employee_id=emp.employee_id)
    record = models.Report.objects.filter(employee_id=emp.employee_id)
    add = models.Additionalpay.objects.filter(payslip__employee_id=emp.employee_id)
    deduction = models.Deduction.objects.filter(payslip__employee_id=emp.employee_id)
    timesheet = models.ReportTimesheet.objects.filter(report__employee_id=emp.employee_id)
    empid = emp.employee_id

    return render(request, 'userapp/user_profile.html',
        {'record':record,
        'empid':empid,
        'add':add,
        'deduction':deduction,
        'timesheet':timesheet,
        'emp':emp,
        'payslip':payslip
        })

class DepartmentListView(ListView):
    template_name = 'userapp/department_list.html'
    context_object_name = 'department_list'
    model = models.Department

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentListView,self).get_context_data(*args,**kwargs)
        dep_list = context['department_list']
        empData = []
        for dep in dep_list:
            total_em = models.Employee.objects.filter(department=dep).count()
            department_head = None
            try:
                department_head = models.Employee.objects.get(department_head=True, department=dep)
            except models.Employee.DoesNotExist:
                department_head = "-"
            total_emp = total_em or 0
            empData.append([dep,total_emp,department_head])
        context['Data'] = empData

        return (context)

def ListofEmpInDep(request, pk):
    data = models.Department.objects.get(pk=pk)
    list_employee = models.Employee.objects.filter(department=data)

    return render(request,'userapp/empdeplist.html',
        {'list_employee':list_employee,
        'data': data,
        })

def SalaryRecordDetail(request,empid ):
    fullname = models.Employee.objects.get(employee_id=empid)
    record = models.Report.objects.filter(employee_id=empid)
    add = models.Additionalpays.objects.filter(report__employee_id=empid)
    deduction = models.Deductions.objects.filter(report__employee_id=empid)
    timesheet = models.ReportTimesheet.objects.filter(report__employee_id=empid)
    data = []
    total_lwop = 0
    total_gross = 0
    total_add = 0
    total_ded = 0
    total_net = 0

    for r in record:
        empAdd = models.Additionalpays.objects.filter(report=r).aggregate(Sum('amount'))['amount__sum']
        empDed = models.Deductions.objects.filter(report=r).aggregate(Sum('amount'))['amount__sum']
        empAdd = empAdd or 0
        empDed = empDed or 0
        empAdd = (round(empAdd,2))
        empDed = (round(empDed,2))
        gross = r.gross_pay - r.lowp_deduction
        net= gross + empAdd - empDed

        total_lwop += r.lowp_deduction
        total_gross += gross
        total_add += empAdd
        total_ded += empDed
        total_net += net

        data.append([r,empAdd,empDed,net,gross])



    return render(request, 'userapp/salary_record_detail.html',
        {'record':record,
        'empid':empid,
        'add':add,
        'deduction':deduction,
        'timesheet':timesheet,
        'fullname':fullname,
        'data':data,
        'total_lwop':total_lwop,
        'total_gross': total_gross,
        "total_add": total_add,
        'total_ded': total_ded,
        'total_net': total_net,
        })


class EmployeeUpdateView(UpdateView):
    model = models.Employee
    form_class = EmployeeForm
    template_name='userapp/employee_update.html'