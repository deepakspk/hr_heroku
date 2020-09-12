from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from django.contrib import admin


# Create your models here.

class Department(models.Model):
    department = models.CharField(unique=True, max_length=40)
    def __str__(self):
        return self.department

class CostCenter(models.Model):
    cost_center = models.CharField(unique=True, max_length=40)
    def __str__(self):
        return self.cost_center

class Hotel(models.Model):
    hotel = models.CharField(unique=True, max_length=40)
    def __str__(self):
        return self.hotel

class Employee(models.Model):
    employee_id         = models.CharField(primary_key=True, max_length=60, unique=True)
    first_name          = models.CharField(max_length=60, blank=True,null=True)
    middle_name         = models.CharField(max_length=60, blank=True,null=True)
    last_name           = models.CharField(max_length=60, blank=True,null=True)
    GENDER_CHOICES      = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'),)
    gender              = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hotel               = models.ForeignKey(Hotel, related_name='hotel_name', on_delete=models.CASCADE,null=True,blank=True)
    DOB                 = models.DateField(null=True, blank=True)
    religion            = models.CharField(max_length=20, null=True, blank=True)
    citizenship         = models.CharField(max_length=20, null=True, blank=True)
    country_birth       = models.CharField(max_length=20, null=True, blank=True)
    email               = models.EmailField(max_length=70, blank=True,null=True)
    phone               = models.IntegerField(null=True, blank=True,default=0)
    uae_address         = models.CharField(max_length=90, null=True, blank=True)
    home_country_phone  = models.CharField(max_length=90, null=True, blank=True)
    home_country_address= models.CharField(max_length=90, null=True, blank=True)
    department          = models.ForeignKey(Department, related_name='dept_name', on_delete=models.CASCADE,null=True,blank=True)
    designation         = models.CharField(max_length=40, null=True, blank=True)
    department_head     = models.BooleanField(default=False)
    joining_date        = models.DateField(null=True, blank=True)
    img                 = models.ImageField(upload_to='pics',null=True,blank=True, default='/static/images/default-user.jpg')
    employee_status_choice     = (('Deployed', 'Deployed'),('Exiting', 'Exiting'),('Resigning', 'Resigning'))
    employee_status            = models.CharField(max_length=10, default=['Active'], choices=employee_status_choice)

    def __str__ (self):
        return str(self.first_name)

    def get_absolute_url(self):
         return reverse("payroll:employee_detail", kwargs={'pk':self.pk})

    @property
    def full_name(self):
        return str(self.first_name) +" "+ str(self.last_name)


class Payslip(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_payslip', on_delete=models.CASCADE, blank=True,null=True)
    basic_salary           =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    housing_allowance      =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    transportation_allowance = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    other                  =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    work_permit_choice     =   (('Uniteam', 'Uniteam'),('Aspen', 'Aspen'),('Uniteam(Br2)', 'Uniteam(Br2)'),)
    work_permit            =   models.CharField(max_length=60, choices=work_permit_choice)
    cost_center            =   models.ForeignKey(CostCenter, related_name='dept_name', on_delete=models.CASCADE,null=True,blank=True)
    mode_of_payment        =   models.CharField(max_length=90, blank=True,null=True,)
    bank_ac                =   models.CharField(max_length=90, blank=True,null=True,)
    PAYMENT_METHOD_CHOICES = (('Bank', 'Bank'),('Lulu Exchange', 'Lulu Exchange'),('Cash', 'Cash'),('Other','Other'),)
    payment_method         =   models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES)
    employee_unique        =   models.CharField(max_length=90, blank=True,null=True,)
    agent_id               =   models.CharField(max_length=90, blank=True,null=True,)
    work_permit_8_digits   =   models.CharField(max_length=8, blank=True,null=True,)
    personal_no_14_digits  =   models.CharField(max_length=14, blank=True,null=True,)
    bank_name_routing      =   models.CharField(max_length=9, blank=True,null=True,)
    def __str__ (self):
        return str(self.employee)

    @property
    def gross_pay(self):
        return self.basic_salary + self.housing_allowance + self.transportation_allowance + self.other

class Clinical(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_clinical', on_delete=models.CASCADE, blank=True,null=True)
    seha_id                =   models.CharField(max_length=90, blank=True,null=True,)
    zoho_id                =   models.CharField(max_length=90, blank=True,null=True,)
    company_email          =   models.EmailField(max_length=70, blank=True,null=True)
    source                 =   models.CharField(max_length=90, blank=True,null=True,)
    source_entity          =   models.CharField(max_length=90, blank=True,null=True,)
    category               =   models.CharField(max_length=90, blank=True,null=True,)
    hiring_status          =   models.CharField(max_length=90, blank=True,null=True,)
    emirates_id            =   models.CharField(max_length=90, blank=True,null=True,)
    Passport_no            =   models.CharField(max_length=90, blank=True,null=True,)
    passport_expiry        =   models.DateField(null=True, blank=True)
    licence_authority      =   models.CharField(max_length=90, blank=True,null=True,)
    doh_licence            =   models.CharField(max_length=90, blank=True,null=True,)
    doh_licence_type_choices = (('Permanent', 'Permanent'),('Temporary', 'Temporary'),)
    doh_licence_type       =   models.CharField(max_length=15, choices=doh_licence_type_choices)
    doh_licence_no         =   models.CharField(max_length=90, blank=True,null=True,)
    previous_company       =   models.CharField(max_length=90, blank=True,null=True,)
    licence_issued_date    =   models.DateField(null=True, blank=True)
    licence_issued_date    =   models.DateField(null=True, blank=True)
    licence_expiry_date    =   models.DateField(null=True, blank=True)
    non_doh_licence_no     =   models.CharField(max_length=90, blank=True,null=True,)
    higest_qualification   =   models.CharField(max_length=90, blank=True,null=True,)
    date_qualified         =   models.DateField(null=True, blank=True)
    clinic_exp_in_5_year_c =   (('TRUE', 'TRUE'),('FALSE', 'FALSE'),)
    clinic_exp_in_5_year   =   models.CharField(max_length=15, choices=clinic_exp_in_5_year_c)
    healthy_fit_c          =   (('TRUE', 'TRUE'),('False', 'FALSE'),)
    healthy_fit            =   models.CharField(max_length=15, choices=healthy_fit_c)
    competencies_c         =   (('TRUE', 'TRUE'),('FALSE', 'FALSE'),)
    competencies           =   models.CharField(max_length=15, choices=competencies_c)
    visa_status_c         =   (('Employer with NOC', 'Employer with NOC'),('Visit/Tourist', 'Visit/Tourist'),('Cancelled', 'Cancelled'),('Spouse/Parent', 'Spouse/Parent'),)
    visa_status           =   models.CharField(max_length=15, choices=visa_status_c)
    previous_visa_sponser =   models.CharField(max_length=90, blank=True,null=True,)
    doh_licence_as        =   models.CharField(max_length=90, blank=True,null=True,)
    work_order            =   models.CharField(max_length=90, blank=True,null=True,)

    def __str__ (self):
        return str(self.employee)


class Timesheet(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_timesheet', on_delete=models.CASCADE, blank=True,null=True)
    month                  =   models.DateField()
    partial_choice         =   (('N', 'N'),('Y', 'Y'))
    partial                =   models.CharField(max_length=60, default=partial_choice[0][0], choices=partial_choice,)
    # hours                  =   models.DecimalField(max_digits=12, decimal_places=2,)
    normal                 =   models.DecimalField(max_digits=12, decimal_places=2,)
    weekend                =   models.DecimalField(max_digits=12, decimal_places=2,)
    holiday                =   models.DecimalField(max_digits=12, decimal_places=2,)
    vacation               =   models.DecimalField(max_digits=12, decimal_places=2,)
    sick                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    lwop                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    total                  =   models.DecimalField(max_digits=12, decimal_places=2,)

    def __str__(self):
        return str(self.employee) +'__'+ str(self.month)

    @property
    def month_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick + self.lwop

    @property
    def pay_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick


class Additionalpay(models.Model):
    payslip               =   models.ForeignKey(Payslip, related_name='additional_pay', on_delete=models.CASCADE,blank=True,null=True)
    ADDITIONALPAY_CHOICES  = (('Annual Air Ticket', 'Annual Air Ticket'),
                              ('Expense Reimbursement', 'Expense Reimbursement'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Bonus', 'Bonus'),
                              ('Overtime/ Holiday Pay', 'Overtime/ Holiday Pay'),
                              ('Other', 'Other'),)
    additional             =   models.CharField(max_length=60, choices=ADDITIONALPAY_CHOICES, blank=True,null=True)
    additional_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                 =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE          = (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    occur                  =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    start_date             =   models.DateField(null=True, blank=True)
    end_date               =   models.DateField(null=True, blank=True)


    def __str__ (self):
        return str(self.additional)

class Deduction(models.Model):
    payslip               =   models.ForeignKey(Payslip, related_name='salary_deduction', on_delete=models.CASCADE,blank=True,null=True)
    DEDUCTION_CHOICES     =   (('Housing Loan', 'Housing Loan'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Traffic Fine', 'Traffic Fine'),
                              ('Loan', 'Loan'),
                              ('Unpaid sick leave', 'Unpaid sick leave'),
                              ('Other', 'Other'),)
    deduction             =   models.CharField(max_length=60, choices=DEDUCTION_CHOICES, blank=True,null=True)
    deduction_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                 =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE          = (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    occur                  =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    start_date             =   models.DateField(null=True, blank=True)
    end_date               =   models.DateField(null=True, blank=True)


    def __str__ (self):
        return str(self.deduction)


class ProcessSalary(models.Model):
    payroll_id      = models.CharField(max_length=90, blank=True,null=True)
    salary_month    = models.DateField(default =datetime.datetime.now)
    employee        = models.ManyToManyField(Payslip, related_name='employee_name')
    start_date      = models.DateField()
    finish_date     = models.DateField()
    SALARY_TYPES    = (('Normal', 'Normal'),
                      ('Adjustment', 'Adjustment'),)
    salary_type     = models.CharField(max_length=60, default=SALARY_TYPES[0][0], choices=SALARY_TYPES, blank=True,null=True)
    SALARY_STATUS   = (('Processing', 'Processing'),
                      ('Processed', 'Processed'),
                      ('Paid', 'Paid'),)
    status          = models.CharField(max_length=60, default=SALARY_STATUS[0][0], choices=SALARY_STATUS, blank=True,null=True)
    employee_count  = models.IntegerField(null=True, blank=True,default=0)
    gross_pay       = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    actual_gross_pay= models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    Additional_pay  = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    deduction       = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    total           = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)

    def __str__(self):
        return str(self.salary_month)

    def get_absolute_url(self):
        return reverse("payroll:process_salary_detail", kwargs={'pk':self.pk})

    @property
    def actual_payroll_id(self):
        return "UMA" + str(self.id)

class Report(models.Model):
    employee_id         = models.CharField(max_length=60)
    first_name          = models.CharField(max_length=60, blank=True,null=True)
    last_name           = models.CharField(max_length=60, blank=True,null=True)
    department          = models.CharField(max_length=60, blank=True,null=True)
    designation         = models.CharField(max_length=40, null=True, blank=True)
    work_permit_choice  = (('Uniteam', 'Uniteam'),('Aspen', 'Aspen'),('Uniteam(Br2)', 'Uniteam(Br2)'),)
    work_permit         = models.CharField(max_length=60, choices=work_permit_choice)
    cost_center         = models.ForeignKey(CostCenter, related_name='department_name', on_delete=models.CASCADE,null=True,blank=True)
    payroll_id          = models.CharField(max_length=90, blank=True,null=True)
    payroll_month       = models.DateField(null=True, blank=True)
    start_date          = models.DateField(null=True, blank=True)
    finish_date         = models.DateField(null=True, blank=True)
    mode_of_payment     = models.CharField(max_length=90, blank=True,null=True)
    basic_salary        = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    housing_allowance   = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    transportation_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    other               = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    lowp_deduction      = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)

    def __str__(self):
        return str(self.employee_id) +'__'+ str(self.payroll_id)

    def get_absolute_url(self):
        return reverse("payroll:salary_report", kwargs={'pk':self.pk})

    @property
    def full_name(self):
        return str(self.first_name) +" "+ str(self.last_name)

    @property
    def gross_pay(self):
        others = self.other or 0
        return self.basic_salary + self.housing_allowance + self.transportation_allowance + others

class Additionalpays(models.Model):
    ADDITIONALPAY_CHOICES  = (('Annual Air Ticket', 'Annual Air Ticket'),
                              ('Expense Reimbursement', 'Expense Reimbursement'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Bonus', 'Bonus'),
                              ('Overtime/ Holiday Pay', 'Overtime/ Holiday Pay'),
                              ('Other', 'Other'),)
    report                 = models.ForeignKey(Report, on_delete=models.CASCADE)
    additional             =   models.CharField(max_length=60, choices=ADDITIONALPAY_CHOICES, blank=True,null=True)
    additional_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                 =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE          = (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    occur                  =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    start_date             =   models.DateField(null=True, blank=True)
    end_date               =   models.DateField(null=True, blank=True)


    def __str__ (self):
        return str(self.additional)

class AdditionalPaysAdmin(admin.ModelAdmin):
    list_display = ('report','additional')

class Deductions(models.Model):
    DEDUCTION_CHOICES     =   (('Housing Loan', 'Housing Loan'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Traffic Fine', 'Traffic Fine'),
                              ('Loan', 'Loan'),
                              ('Other', 'Other'),)
    report                =   models.ForeignKey(Report, on_delete=models.CASCADE)
    deduction             =   models.CharField(max_length=60, choices=DEDUCTION_CHOICES, blank=True,null=True)
    deduction_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE         =  (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    occur                 =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    start_date            =   models.DateField(null=True, blank=True)
    end_date              =   models.DateField(null=True, blank=True)

    def __str__ (self):
        return str(self.deduction)


class ReportTimesheet(models.Model):
    report                 =   models.ForeignKey(Report, on_delete=models.CASCADE)
    employee               =   models.CharField(max_length=60,)
    month                  =   models.DateField()
    partial                =   models.CharField(max_length=60,)
    normal                 =   models.DecimalField(max_digits=12, decimal_places=2,)
    weekend                =   models.DecimalField(max_digits=12, decimal_places=2,)
    holiday                =   models.DecimalField(max_digits=12, decimal_places=2,)
    vacation               =   models.DecimalField(max_digits=12, decimal_places=2,)
    sick                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    lwop                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    total                  =   models.DecimalField(max_digits=12, decimal_places=2,)

    def __str__(self):
        return str(self.employee) +'__'+ str(self.month)

    @property
    def month_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick + self.lwop

    @property
    def pay_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick


class LaborContract(models.Model):
    employee               = models.ForeignKey(Employee, related_name='employee_labourcontract', on_delete=models.CASCADE, blank=True,null=True)
    contract_issue_date    = models.DateField(null=True, blank=True)

    contract_collected     = models.BooleanField(default=False)    
    contract_collected_date= models.DateField(null=True, blank=True)    
    passport_collected     = models.BooleanField(default=False)
    passport_collect_date  = models.DateField(null=True, blank=True)
    medical_done           = models.BooleanField(default=False)
    medical_date           = models.DateField(null=True, blank=True)
    passport_receive_date  = models.DateField(null=True, blank=True)
    passport_returned      = models.BooleanField(default=False)
    passport_returned_date = models.DateField(null=True, blank=True)
    note                   = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return str(self.employee)

class WorkPermit(models.Model):
    employee               = models.ForeignKey(Employee, related_name='employee_workpermit', on_delete=models.CASCADE, blank=True,null=True)
    contract_issue_date    = models.DateField(null=True, blank=True)
    contract_collected     = models.BooleanField(default=False)    
    contract_collected_date = models.DateField(null=True, blank=True)
    note                    = models.CharField(null=True, blank=True, max_length=300)
    
    def __str__(self):
        return str(self.employee)

class EidCollect(models.Model):
    employee               = models.ForeignKey(Employee, related_name='employee_eidcollect', on_delete=models.CASCADE, blank=True,null=True)
    eid_requested_date     = models.DateField(null=True, blank=True)
    collected              = models.BooleanField(default=False)
    eid_collected_date     = models.DateField(null=True, blank=True)
    returned               = models.BooleanField(default=False)
    eid_returned_date      = models.DateField(null=True, blank=True)
    note                   = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return str(self.employee)

class NewEid(models.Model):
    employee               = models.ForeignKey(Employee, related_name='employee_neweid', on_delete=models.CASCADE, blank=True,null=True)
    eid_received_date      = models.DateField(null=True, blank=True)
    collected              = models.BooleanField(default=False)
    eid_collected_date     = models.DateField(null=True, blank=True)
    note                   = models.CharField(null=True, blank=True, max_length=300)


    def __str__(self):
        return str(self.employee)