# Generated by Django 4.0 on 2022-03-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_applicantprofile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='pin',
            field=models.CharField(max_length=6),
        ),
    ]
