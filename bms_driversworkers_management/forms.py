from django import forms
from bms_driversworkers_management.models import DriverSchedule, Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'contact_no', 'status', 'job_title', 'date_of_hire', 'photo']
        widgets = {
            'date_of_hire': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_year(self):
        date_of_hire = self.cleaned_data.get('date_of_hire')
        if not (1900 <= date_of_hire.year <= 2099):  # If it's a DateField, use `year.year`
            raise forms.ValidationError("Date of hire must be between 1900 and 2099.")
        return date_of_hire

class DriverScheduleForm(forms.ModelForm):
    class Meta:
        model = DriverSchedule
        fields = ['driver', 'bus', 'start_time', 'end_time', 'days_active']