# Generated by Django 4.2.3 on 2023-07-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_uploaded_files_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password1',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='password2',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
