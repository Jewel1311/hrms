# Generated by Django 4.0 on 2022-03-12 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_designations'),
        ('base', '0007_alter_department_options_and_more'),
        ('employees', '0020_alter_employeeprofile_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='department',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.department'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='designation',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.designations'),
        ),
    ]