# Generated by Django 4.0 on 2022-03-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_jobs_withdraw_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
    ]
