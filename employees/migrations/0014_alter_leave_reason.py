# Generated by Django 4.0 on 2022-03-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_leave_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.CharField(max_length=200),
        ),
    ]
