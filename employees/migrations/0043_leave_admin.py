# Generated by Django 3.2.12 on 2022-04-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0042_auto_20220401_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]