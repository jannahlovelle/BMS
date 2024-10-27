# bms_app/migrations/0008_schedule.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bms_app', '0007_userprofile'),  # Adjust this to your last migration
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('sched_id', models.AutoField(primary_key=True, serialize=False)),
                ('route', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('status', models.CharField(
                    max_length=50,
                    choices=[
                        ('on_standby', 'On Standby'),
                        ('in_transit', 'In Transit'),
                        ('arrived', 'Arrived'),
                    ]
                )),
                ('bus', models.ForeignKey(on_delete=models.CASCADE, related_name='schedules', to='bms_app.Bus')),
            ],
        ),
    ]
