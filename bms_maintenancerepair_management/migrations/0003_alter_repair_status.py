# Generated by Django 5.1.2 on 2024-12-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_maintenancerepair_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='status',
            field=models.CharField(choices=[('Under Maintenance', 'Under Maintenance'), ('Done', 'Done')], max_length=100),
        ),
    ]
