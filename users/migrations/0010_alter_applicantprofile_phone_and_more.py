# Generated by Django 4.0 on 2022-02-08 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_applicantprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be a digit. Up to 10 digits allowed.', regex='^\\+?1?\\d{9,10}$')]),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='pin',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Pin must be a digit. Up to 6 digits allowed.', regex='^\\+?1?\\d{9,6}$')]),
        ),
    ]
