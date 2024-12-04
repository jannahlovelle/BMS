from django import forms

from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Schedule


class ScheduleForm(forms.ModelForm):
    bus = forms.ModelChoiceField(
        queryset=Bus.objects.all(),
        to_field_name='plate_number',
        label='Select Bus',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Schedule
        fields = ['bus', 'employee' ,'route', 'notes']
        
