
from django import forms
from .models import Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['plate_number', 'model', 'make', 'year', 'capacity', 'status']
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date'})
        }
    
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if not (1900 <= year.year <= 2099):  # If it's a DateField, use `year.year`
            raise forms.ValidationError("Year must be between 1900 and 2099.")
        return year