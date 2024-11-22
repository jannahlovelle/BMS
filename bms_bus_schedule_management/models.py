from django.db import models
from marshmallow import ValidationError

from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee

# Create your models here.
class Schedule(models.Model):
    sched_id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)  # Allow NULL values
    status = models.CharField(max_length=50, choices=[
        ('on_standby', 'On Standby'),
        ('in_transit', 'In Transit'),
        ('arrived', 'Arrived'),
    ])
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedules', null=True)  # Add this line

    # New fields
    frequency = models.CharField(max_length=50, null=True, blank=True)  # e.g., daily, weekly
    last_updated = models.DateTimeField(auto_now=True)  # Automatically updates when the schedule is saved
    notes = models.TextField(null=True, blank=True)  # Additional notes about the schedule

    def __str__(self):
        return self.route

    def clean(self):
        # Check if arrival_time is provided before comparing
        if self.arrival_time and self.arrival_time <= self.departure_time:
            raise ValidationError('Arrival time must be after departure time.')


    # New fields
    frequency = models.CharField(max_length=50, null=True, blank=True)  # e.g., daily, weekly
    last_updated = models.DateTimeField(auto_now=True)  # Automatically updates when the schedule is saved
    notes = models.TextField(null=True, blank=True)  # Additional notes about the schedule

    def __str__(self):
        return self.route

    def clean(self):
        # Check if arrival_time is provided before comparing
        if self.arrival_time and self.arrival_time <= self.departure_time:
            raise ValidationError('Arrival time must be after departure time.')