# Generated by Django 2.2.1 on 2020-03-01 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0016_auto_20200228_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_timesheet', to='payroll.Payslip'),
        ),
    ]
