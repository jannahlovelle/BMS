from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import User
from marshmallow import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Employee(models.Model):
    JOB_TITLE_CHOICES = [
        ('driver', 'Driver'),
        ('mechanic', 'Mechanic'),
    ]
    EMPLOYEE_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    employee_id = models.AutoField(primary_key=True)
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)  # Added middle name
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    contact_no = models.CharField(max_length=30, null=True, blank=True)  # Added contact number
    status = models.CharField(max_length=100, choices=EMPLOYEE_STATUS_CHOICES, null=True, blank=True)  # Added status field
    job_title = models.CharField(max_length=100, choices=JOB_TITLE_CHOICES, null=True, blank=True)  # Added job title field
    date_of_hire = models.DateField(default=timezone.now)  # Added date of hire field
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)  # Field for photo

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Bus(models.Model):
    BUS_STATUS_CHOICES = [
        ('on_standby', 'On Standby'),
        ('in_transit', 'In Transit'),
        ('under_maintenance', 'Under Maintenance'),
    ]

    bus_id = models.AutoField(primary_key=True)
    plate_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.DateField()
    capacity = models.IntegerField()
    status = models.CharField(max_length=50, choices=BUS_STATUS_CHOICES)  # Use choices here
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.plate_number} ({self.model})"
        return self.plate_number

# Updated 03/11/2024
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
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='schedules')  # Add related_name
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
        
class Repair(models.Model):
    repair_desc = models.CharField(max_length=100)
    start_date = models.DateField()
    est_completion = models.DateField()
    status = models.CharField(max_length=100, choices = [('under_maintenance', 'Under Maintenance'), ('done', 'Done')])
    repair_cost = models.FloatField()
    parts_used = models.CharField(max_length=255)
    follow_action = models.CharField(max_length=255)
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  

class DriverSchedule(models.Model):
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_active = models.CharField(max_length=50, help_text="E.g., 'Mon-Fri' or 'Mon,Wed,Fri'")

    def __str__(self):
        return f"{self.driver} - {self.bus} ({self.start_time} to {self.end_time} on {self.days_active})"
