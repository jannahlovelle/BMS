from django import forms
from bms_user_authentication.models import UserProfile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        user_profile = super(UserProfileForm, self).save(commit=False)
        user = user_profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile.save()
        return user_profile

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']

class LoginForm(AuthenticationForm):
    pass