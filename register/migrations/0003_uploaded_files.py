# Generated by Django 4.2.3 on 2023-07-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploaded_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('visibility', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('year_of_pblish', models.DateField(blank=True, null=True)),
                ('display_picture', models.FileField(upload_to='')),
            ],
        ),
    ]
