from django.contrib import admin
from .models import Bus, Employee, Schedule
# Register your models here.

admin.site.register(Employee)
admin.site.register(Bus)
admin.site.register(Schedule)
