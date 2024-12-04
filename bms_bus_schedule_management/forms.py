from django import forms

from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Schedule


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['bus', 'employee' ,'route', 'notes']