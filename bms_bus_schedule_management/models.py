from django.db import models
from marshmallow import ValidationError

from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee

class Schedule(models.Model):
    sched_id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=100)
    departure_time = models.DateTimeField(null=True, blank=True)  # Allow NULL values
    arrival_time = models.DateTimeField(null=True, blank=True)  # Allow NULL values
    status = models.CharField(max_length=50, choices=[
        ('on_standby', 'On Standby'),
        ('in_transit', 'In Transit'),
        ('arrived', 'Arrived'),
    ], default='on_standby')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedules', null=True, blank=True, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    # New fields
    frequency = models.CharField(max_length=50, null=True, blank=True, default=1)  # e.g., daily, weekly
    notes = models.TextField(null=True, blank=True)  # Additional notes about the schedule

    def __str__(self):
        return self.route

    def clean(self):
        # Check if arrival_time is provided before comparing
        if self.arrival_time and self.arrival_time <= self.departure_time:
            raise ValidationError('Arrival time must be after departure time.')
    
    def save(self, *args, **kwargs):
        # Create a history record only if arrival_time is set
        if self.arrival_time:
            ScheduleHistory.objects.create(
                schedule=self,
                route=self.route,
                departure_time=self.departure_time,
                arrival_time=self.arrival_time,
                status=self.status,
                bus=self.bus,
                employee=self.employee,
                frequency=self.frequency,
                notes=self.notes
            )
        super().save(*args, **kwargs)

class ScheduleHistory(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='history')
    route = models.CharField(max_length=100)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.schedule.route} at {self.updated_at}"

