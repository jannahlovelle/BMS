from django import forms
from bms_maintenancerepair_management.models import Repair
from django.forms import DateTimeInput

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'repair_desc',
            'start_date',
            'est_completion',
            'status',
            'repair_cost',
            'parts_used',
            'follow_action',
            'bus',
            'employee',
        ]
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'est_completion': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # Optional: you can customize how fields look in the form (like for the status field).
    STATUS_CHOICES = [
        ('Under Maintenance', 'Under Maintenance'),
        ('Done', 'Done'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)

    # Optional: You can also customize labels for better readability.
    repair_desc = forms.CharField(max_length=100, label="Repair Description")
    repair_cost = forms.FloatField(label="Repair Cost")
    parts_used = forms.CharField(max_length=255, label="Parts Used")
    follow_action = forms.CharField(max_length=255, label="Follow-up Action")