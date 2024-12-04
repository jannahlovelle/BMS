from django.db import models
from django.core.exceptions import ValidationError  # Correct import

from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee


class Schedule(models.Model):
    sched_id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=100)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('on_standby', 'On Standby'),
        ('in_transit', 'In Transit'),
        ('arrived', 'Arrived'),
    ], default='on_standby')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedules', null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    frequency = models.CharField(max_length=50, null=True, blank=True, default=1)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.route

    def clean(self):
        if self.arrival_time and self.departure_time:
            if self.arrival_time <= self.departure_time:
                raise ValidationError("Arrival time must be later than departure time.")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.arrival_time:
            ScheduleHistory.objects.create(
                schedule=self,  # Now the schedule is saved
                route=self.route,
                departure_time=self.departure_time,
                arrival_time=self.arrival_time,
                status=self.status,
                bus=self.bus,
                employee=self.employee,
                frequency=self.frequency,
                notes=self.notes
            )


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