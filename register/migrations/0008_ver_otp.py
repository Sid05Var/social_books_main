# Generated by Django 4.2.3 on 2023-07-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_uploaded_files_visibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='ver_otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_otp', models.CharField(max_length=200)),
            ],
        ),
    ]