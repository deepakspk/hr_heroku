# Generated by Django 2.2.1 on 2020-02-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0009_auto_20200210_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_status',
            field=models.BooleanField(default=True),
        ),
    ]
