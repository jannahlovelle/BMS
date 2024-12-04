from django.db import models

from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee

# Create your models here.
class Repair(models.Model):
    repair_desc = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True, blank=True)
    est_completion = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices = [('Under Maintenance', 'Under Maintenance'), ('Done', 'Done')])
    repair_cost = models.FloatField()
    parts_used = models.CharField(max_length=255)
    follow_action = models.CharField(max_length=255)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  