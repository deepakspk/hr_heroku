# Generated by Django 2.2.1 on 2020-07-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0030_eidcollect_hotel_laborcontract_workpermit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eidcollect',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='laborcontract',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='workpermit',
            name='hotel',
        ),
        migrations.AddField(
            model_name='employee',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_name', to='payroll.Hotel'),
        ),
    ]
