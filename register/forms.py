from datetime import date
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import uploaded_files
# from .models import ver_otp


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
     
        fields = ( 'username',
'email', 'gender', 'fullname', 'password1', 'password2','dob', 'visibility')
        widgets = {
            'dob': forms.NumberInput(attrs={'class': 'form-control'}),
            'visibility': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'gender': forms.ChoiceField(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': "form-control", 'type': 'password', 'name': "password1",'id': "id_password1" }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control ",
                'placeholder': 'Password',
                'type': 'password',
                'name': 'password2',
                'id' : "id_password2" , 
                'template_name': 'register.html',
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', })
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', })
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        year_of_birth = self.cleaned_data['dob']
        age = calculate_age(year_of_birth)
        instance.age = age
        if commit:
            instance.save()

        return instance
        
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
        
def calculate_age(year_of_birth):
    current_year = date.today().year
    age = current_year - year_of_birth
    return age