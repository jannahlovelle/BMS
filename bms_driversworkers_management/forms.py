from django import forms
from bms_driversworkers_management.models import DriverSchedule, Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'contact_no', 'status', 'job_title', 'date_of_hire', 'photo']

class DriverScheduleForm(forms.ModelForm):
    class Meta:
        model = DriverSchedule
        fields = ['driver', 'bus', 'start_time', 'end_time', 'days_active']