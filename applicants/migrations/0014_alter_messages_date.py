# Generated by Django 3.2.12 on 2022-04-04 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0013_alter_messages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 4, 16, 40, 15, 291719)),
        ),
    ]
