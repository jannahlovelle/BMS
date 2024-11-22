

from django import forms
from bms_user_authentication.models import UserProfile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



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