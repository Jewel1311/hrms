# Generated by Django 4.0 on 2022-03-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0025_remove_employeeprofile_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
