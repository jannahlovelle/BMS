# Generated by Django 5.1.1 on 2024-11-22 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bms_bus_information_management', '0001_initial'),
        ('bms_driversworkers_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('sched_id', models.AutoField(primary_key=True, serialize=False)),
                ('route', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('on_standby', 'On Standby'), ('in_transit', 'In Transit'), ('arrived', 'Arrived')], max_length=50)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_bus_information_management.bus')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bms_driversworkers_management.employee')),
            ],
        ),
    ]
