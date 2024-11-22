
from django import forms
from bms_bus_information_management.models import Bus


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['plate_number', 'model', 'make', 'year', 'capacity', 'status']