from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
   
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    # Any additional fields or methods specific to your user model

    def __str__(self):
        return self.email
    
class uploaded_files(models.Model):
    Name = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    visibility = models.BooleanField(default=True)
    cost = models.IntegerField()
    year_of_pblish = models.DateField(null=True, blank=True)
    display_picture = models.FileField()
   
    def __str__(self):
        return self.Name
    

# class ver_otp(models.Model):
#     enter_otp = models.CharField(max_length=200)
    
    # def __str__(self):
    #     return self.enter_otp