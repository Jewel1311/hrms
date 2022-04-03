from django.db import models
from users.models import Newuser

class Salary(models.Model):
    basic_pay = models.DecimalField(max_digits=7, decimal_places=2)
    hra = models.BooleanField(default=False)
    ta = models.BooleanField(default=False)
    pf = models.BooleanField(default=False)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)

class Designations(models.Model):
    designation = models.CharField(max_length=60)

    def __str__(self):
        return self.designation

class Payroll(models.Model):
    basic = models.DecimalField(max_digits=7, decimal_places=2)
    hra = models.DecimalField(max_digits=6, decimal_places=2)
    ta = models.DecimalField(max_digits=6, decimal_places=2)
    pf = models.DecimalField(max_digits=6, decimal_places=2)
    other_benefits = models.DecimalField(max_digits=6, decimal_places=2)
    other_deductions = models.DecimalField(max_digits=6, decimal_places=2)
    net_salary = models.DecimalField(max_digits=7, decimal_places=2) 
    date = models.DateField()
    user = user = models.ForeignKey(Newuser, on_delete=models.CASCADE)

