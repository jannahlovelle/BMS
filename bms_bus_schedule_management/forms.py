from django import forms

from bms_bus_information_management.models import Bus
from bms_bus_schedule_management.models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['bus', 'employee', 'route', 'departure_time', 'arrival_time', 'status', 'frequency', 'notes']
        widgets = {
            'bus': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'route': forms.TextInput(attrs={'class': 'form-control'}),
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        departure_time = cleaned_data.get('departure_time')
        arrival_time = cleaned_data.get('arrival_time')

        if arrival_time and departure_time and arrival_time <= departure_time:
            raise forms.ValidationError("Arrival time must be after departure time.")
        return cleaned_data