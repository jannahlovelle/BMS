from django.contrib import admin
from .models import Bus, DriverSchedule, Employee, Repair, Schedule
# Register your models here.

admin.site.register(Employee)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Repair)
admin.site.register(DriverSchedule)