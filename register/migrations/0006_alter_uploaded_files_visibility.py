# Generated by Django 4.2.3 on 2023-07-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_uploaded_files_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded_files',
            name='visibility',
            field=models.BooleanField(),
        ),
    ]
