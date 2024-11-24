from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

from bms_bus_information_management.models import Bus

# Create your models here.
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
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)  # Added email field
    contact_no = models.CharField(max_length=30, null=True, blank=True)  # Added contact number
    status = models.CharField(max_length=100, choices=EMPLOYEE_STATUS_CHOICES, null=True, blank=True)  # Added status field
    job_title = models.CharField(max_length=100, choices=JOB_TITLE_CHOICES, null=True, blank=True)  # Added job title field
    date_of_hire = models.DateField(default=timezone.now)  # Added date of hire field
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)  # Field for photo

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class DriverSchedule(models.Model):
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_active = models.CharField(max_length=50, help_text="E.g., 'Mon-Fri' or 'Mon,Wed,Fri'")

    def __str__(self):
        return f"{self.driver} - {self.bus} ({self.start_time} to {self.end_time} on {self.days_active})"
