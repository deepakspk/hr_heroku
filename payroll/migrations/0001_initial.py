# Generated by Django 2.2.1 on 2020-01-28 14:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=20, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=20, null=True)),
                ('country_birth', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('phone', models.IntegerField(blank=True, default=0, null=True)),
                ('uae_address', models.CharField(blank=True, max_length=90, null=True)),
                ('home_country_phone', models.CharField(blank=True, max_length=90, null=True)),
                ('home_country_address', models.CharField(blank=True, max_length=90, null=True)),
                ('designation', models.CharField(blank=True, max_length=40, null=True)),
                ('department_head', models.BooleanField(default=False)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('work_permit', models.CharField(blank=True, max_length=90, null=True)),
                ('img', models.ImageField(blank=True, default='/static/images/default-user.jpg', null=True, upload_to='pics')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_name', to='payroll.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(blank=True, max_length=90, null=True, unique=True)),
                ('basic_salary', models.IntegerField(blank=True, default=0, null=True)),
                ('housing_allowance', models.IntegerField(blank=True, default=0, null=True)),
                ('transportation_allowance', models.IntegerField(blank=True, default=0, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_payslip', to='payroll.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('department', models.CharField(blank=True, max_length=60, null=True)),
                ('work_permit', models.CharField(blank=True, max_length=90, null=True)),
                ('payroll_id', models.CharField(blank=True, max_length=90, null=True)),
                ('payroll_month', models.DateField(blank=True, null=True)),
                ('mode_of_payment', models.CharField(blank=True, max_length=90, null=True, unique=True)),
                ('basic_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('housing_allowance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('transportation_allowance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payroll_id', models.CharField(blank=True, max_length=90, null=True)),
                ('salary_month', models.DateField(default=datetime.datetime.now)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('salary_type', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Adjustment', 'Adjustment')], default='Normal', max_length=60, null=True)),
                ('status', models.CharField(blank=True, choices=[('Processing', 'Processing'), ('Processed', 'Processed'), ('Paid', 'Paid')], default='Processing', max_length=60, null=True)),
                ('gross_pay', models.IntegerField(blank=True, default=0, null=True)),
                ('Additional_pay', models.IntegerField(blank=True, default=0, null=True)),
                ('deduction', models.IntegerField(blank=True, default=0, null=True)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('employee', models.ManyToManyField(related_name='employee_name', to='payroll.Payslip')),
            ],
        ),
        migrations.CreateModel(
            name='Deductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deduction', models.CharField(blank=True, choices=[('Housing Loan', 'Housing Loan'), ('Salary Advance', 'Salary Advance'), ('Traffic Fine', 'Traffic Fine'), ('Loan', 'Loan'), ('Other', 'Other')], max_length=60, null=True)),
                ('deduction_label', models.CharField(blank=True, max_length=90, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('occur', models.CharField(blank=True, choices=[('Once', 'Once'), ('Monthly', 'Monthly')], max_length=60, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deduction', models.CharField(blank=True, choices=[('Housing Loan', 'Housing Loan'), ('Salary Advance', 'Salary Advance'), ('Traffic Fine', 'Traffic Fine'), ('Loan', 'Loan'), ('Other', 'Other')], max_length=60, null=True)),
                ('deduction_label', models.CharField(blank=True, max_length=90, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('occur', models.CharField(blank=True, choices=[('Once', 'Once'), ('Monthly', 'Monthly')], max_length=60, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('payslip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salary_deduction', to='payroll.Payslip')),
            ],
        ),
        migrations.CreateModel(
            name='Additionalpays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional', models.CharField(blank=True, choices=[('Annual Air Ticket', 'Annual Air Ticket'), ('Expense Reimbursement', 'Expense Reimbursement'), ('Bonus', 'Bonus'), ('Other', 'Other')], max_length=60, null=True)),
                ('additional_label', models.CharField(blank=True, max_length=90, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('occur', models.CharField(blank=True, choices=[('Once', 'Once'), ('Monthly', 'Monthly')], max_length=60, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Additionalpay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional', models.CharField(blank=True, choices=[('Annual Air Ticket', 'Annual Air Ticket'), ('Expense Reimbursement', 'Expense Reimbursement'), ('Bonus', 'Bonus'), ('Other', 'Other')], max_length=60, null=True)),
                ('additional_label', models.CharField(blank=True, max_length=90, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('occur', models.CharField(blank=True, choices=[('Once', 'Once'), ('Monthly', 'Monthly')], max_length=60, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('payslip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_pay', to='payroll.Payslip')),
            ],
        ),
    ]
