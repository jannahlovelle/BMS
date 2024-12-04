from django import forms

from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Schedule
from bms_driversworkers_management.models import Employee


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['bus', 'employee' ,'route', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ScheduleForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['employee'].queryset = Employee.objects.filter(user=user, status='active', job_title='driver')