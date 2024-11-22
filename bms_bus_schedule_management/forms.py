from django import forms

from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Schedule


class ScheduleForm(forms.ModelForm):
    bus = forms.ModelChoiceField(
        queryset=Bus.objects.all(),
        to_field_name='plate_number',  # Assuming plate_number is the field you want to display
        label='Select Bus'
    )

    class Meta:
        model = Schedule
        fields = ['route', 'departure_time', 'arrival_time', 'status', 'bus', 'frequency', 'notes']
