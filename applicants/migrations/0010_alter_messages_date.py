# Generated by Django 3.2.12 on 2022-04-03 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0009_alter_messages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 19, 7, 53, 416124)),
        ),
    ]
