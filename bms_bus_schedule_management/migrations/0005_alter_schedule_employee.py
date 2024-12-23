# Generated by Django 5.1.1 on 2024-11-23 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_bus_schedule_management', '0004_alter_schedule_employee'),
        ('bms_driversworkers_management', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bms_driversworkers_management.employee'),
        ),
    ]
