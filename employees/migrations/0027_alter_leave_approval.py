# Generated by Django 4.0 on 2022-03-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0026_alter_employeeprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='approval',
            field=models.CharField(default='pending', max_length=12),
        ),
    ]