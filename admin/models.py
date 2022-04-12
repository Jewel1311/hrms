from django.db import models
from users.models import Newuser

class Salary(models.Model):
    basic_pay = models.FloatField()
    hra = models.BooleanField(default=False)
    ta = models.BooleanField(default=False)
    pf = models.BooleanField(default=False)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)

class Designations(models.Model):
    designation = models.CharField(max_length=60)

    def __str__(self):
        return self.designation

class Payroll(models.Model):
    basic = models.FloatField()
    hra = models.FloatField()
    ta = models.FloatField()
    pf = models.FloatField()
    other_benefits = models.FloatField()
    other_deductions = models.FloatField()
    net_salary = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=12,default='pending')
    user = user = models.ForeignKey(Newuser, on_delete=models.CASCADE)

class Holidays(models.Model):
    date = models.DateField()
    reason = models.TextField()