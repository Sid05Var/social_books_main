from django.db import models

# Create your models here.

class uploaded_files(models.Model):
    Name = models.CharField(max_length=200)
    visibility = models.CharField(max_length=200)
    cost = models.IntegerField()
    year_of_pblish = models.DateField(null=True, blank=True)
    display_picture = models.FileField()
   
    def __str__(self):
        return self.Name

