# Generated by Django 2.2.1 on 2020-07-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0031_auto_20200728_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laborcontract',
            old_name='contract_date',
            new_name='contract_issue_date',
        ),
        migrations.RenameField(
            model_name='laborcontract',
            old_name='passport_date',
            new_name='contract_sign_date',
        ),
        migrations.RenameField(
            model_name='laborcontract',
            old_name='passport',
            new_name='passport_collect',
        ),
        migrations.AddField(
            model_name='laborcontract',
            name='passport_collect_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workpermit',
            name='contract_issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
