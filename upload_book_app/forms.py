from django import forms
from .models import uploaded_files


class Profile_form(forms.ModelForm):
    
    class Meta:
        model = uploaded_files
        fields = {
            'Name',
            'visibility',
            'cost',
            'year_of_pblish',
            'display_picture',
        }