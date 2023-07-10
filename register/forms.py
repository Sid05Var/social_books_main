from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import uploaded_files
# from .models import ver_otp

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 'username',
'email', 'gender', 'fullname','password1','password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            # 'password1':forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2':forms.PasswordInput(attrs={'class': 'form-control'}),
            'password1':forms.PasswordInput(attrs={
            'class': "form-control ",
            'type': 'password',
            'name': 'password1',
            'placeholder': 'Password',
            'id' : "id_password1" , 
        }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control ",
                'placeholder': 'Password',
                'type': 'password',
                'name': 'password2',
                'id' : "id_password2" , 
            }),
        }
        
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
            'book_image',
        }