from django.contrib import admin

# Register your models here.

from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Schedule
from bms_maintenancerepair_management.models import Repair
from bms_driversworkers_management.models import Employee, DriverSchedule
# Register your models here.

admin.site.register(Employee)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Repair)
admin.site.register(DriverSchedule)