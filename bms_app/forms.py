from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from bms_app.models import Bus, Employee, Schedule, UserProfile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']  # Only include the profile_picture field

    def __str__(self):
        return f"UserProfileForm for {self.instance.user.username}"  # Optional

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']  # Include fields to edit

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']

class LoginForm(AuthenticationForm):
    pass

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'contact_no', 'status', 'job_title', 'date_of_hire', 'photo']

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['plate_number', 'model', 'make', 'year', 'capacity', 'status']



from django import forms
from .models import Repair, Schedule, Bus

class ScheduleForm(forms.ModelForm):
    bus = forms.ModelChoiceField(
        queryset=Bus.objects.all(),
        to_field_name='plate_number',  # Assuming plate_number is the field you want to display
        label='Select Bus'
    )

    class Meta:
        model = Schedule
        fields = ['route', 'departure_time', 'arrival_time', 'status', 'bus', 'frequency', 'notes']

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
