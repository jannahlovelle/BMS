from django import forms

from bms_maintenancerepair_management.models import Repair


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
            'employee',  # Use 'employee' here, not 'employee_id'
        ]
