from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import uploaded_files
# from .models import ver_otp

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 'username',
'email', 'gender', 'fullname')
        
# class V_otpform(forms.ModelForm):
#     class Meta:
#         model = ver_otp
#         fields= ( 'enter_otp',)
      
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