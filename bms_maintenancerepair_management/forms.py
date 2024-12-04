from django import forms
from bms_driversworkers_management.models import Employee
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

    STATUS_CHOICES = [
        ('under_maintenance', 'Under Maintenance'),
        ('done', 'Done'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    repair_desc = forms.CharField(max_length=100, label="Repair Description")
    repair_cost = forms.FloatField(label="Repair Cost")
    parts_used = forms.CharField(max_length=255, label="Parts Used")
    follow_action = forms.CharField(max_length=255, label="Follow-up Action")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RepairForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['employee'].queryset = Employee.objects.filter(user=user, status='active', job_title='mechanic')