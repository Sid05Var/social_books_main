# Generated by Django 4.2.3 on 2023-07-11 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_customuser_password1_customuser_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password2',
        ),
    ]
