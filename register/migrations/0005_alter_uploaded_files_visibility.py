# Generated by Django 4.2.3 on 2023-07-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_uploaded_files_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded_files',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]