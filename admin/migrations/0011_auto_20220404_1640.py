# Generated by Django 3.2.12 on 2022-04-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0010_auto_20220404_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='basic',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='hra',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='net_salary',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='other_benefits',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='other_deductions',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='pf',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='ta',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='salary',
            name='basic_pay',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
