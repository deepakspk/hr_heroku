# Generated by Django 2.2.1 on 2020-07-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0034_auto_20200729_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workpermit',
            old_name='contract',
            new_name='contract_collected',
        ),
        migrations.RemoveField(
            model_name='laborcontract',
            name='contract',
        ),
        migrations.AddField(
            model_name='eidcollect',
            name='eid_collected_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eidcollect',
            name='eid_requested_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eidcollect',
            name='eid_returned_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
