# Generated by Django 2.2.1 on 2020-06-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0028_clinical_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinical',
            name='clinic_exp_in_5_year',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='clinical',
            name='competencies',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='clinical',
            name='healthy_fit',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('False', 'FALSE')], max_length=15),
        ),
    ]
