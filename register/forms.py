from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import uploaded_files

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 'username',
'email', 'gender', 'fullname')
        
        
class Profile_form(forms.ModelForm):
    
    class Meta:
        model = uploaded_files
        fields = {
            'Name',
            'Title',
            'visibility',
            'cost',
            'year_of_pblish',
            'display_picture',
        }