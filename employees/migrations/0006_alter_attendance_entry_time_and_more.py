# Generated by Django 4.0 on 2022-03-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='entry_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='exit_time',
            field=models.TimeField(null=True),
        ),
    ]
