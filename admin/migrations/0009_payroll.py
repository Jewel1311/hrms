# Generated by Django 3.2.12 on 2022-04-03 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0008_alter_salary_basic_pay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.DecimalField(decimal_places=2, max_digits=7)),
                ('hra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ta', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pf', models.DecimalField(decimal_places=2, max_digits=6)),
                ('other_benefits', models.DecimalField(decimal_places=2, max_digits=6)),
                ('other_deductions', models.DecimalField(decimal_places=2, max_digits=6)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
