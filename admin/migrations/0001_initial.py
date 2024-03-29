# Generated by Django 4.0 on 2022-03-12 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_applicantprofile_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_pay', models.IntegerField()),
                ('hra', models.BooleanField(default=False)),
                ('ta', models.BooleanField(default=False)),
                ('pf', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.newuser')),
            ],
        ),
    ]
