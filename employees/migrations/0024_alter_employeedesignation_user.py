# Generated by Django 4.0 on 2022-03-12 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_applicantprofile_phone_and_more'),
        ('employees', '0023_employeedesignation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedesignation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.newuser'),
        ),
    ]