# Generated by Django 3.2.12 on 2022-04-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0037_yearcounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='leave',
            field=models.BooleanField(default=False),
        ),
    ]
