from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

# Create your models here.
class Bus(models.Model):
    BUS_STATUS_CHOICES = [
        ('on_standby', 'On Standby'),
        ('in_transit', 'In Transit'),
        ('under_maintenance', 'Under Maintenance'),
    ]

    bus_id = models.AutoField(primary_key=True)
    plate_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.DateField()
    capacity = models.IntegerField()
    status = models.CharField(max_length=50, choices=BUS_STATUS_CHOICES, default='on_standby')  # Use choices here
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.plate_number} ({self.model})"
        return self.plate_number