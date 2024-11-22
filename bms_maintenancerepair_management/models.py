from django.db import models

from bms_bus_information_management.models import Bus
from bms_driversworkers_management.models import Employee

# Create your models here.
class Repair(models.Model):
    repair_desc = models.CharField(max_length=100)
    start_date = models.DateField()
    est_completion = models.DateField()
    status = models.CharField(max_length=100, choices = [('under_maintenance', 'Under Maintenance'), ('done', 'Done')])
    repair_cost = models.FloatField()
    parts_used = models.CharField(max_length=255)
    follow_action = models.CharField(max_length=255)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  