from django.db import models
from users.models import Newuser

class Salary(models.Model):
    basic_pay = models.IntegerField()
    hra = models.BooleanField(default=False)
    ta = models.BooleanField(default=False)
    pf = models.BooleanField(default=False)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)

class Designations(models.Model):
    designation = models.CharField(max_length=60)

    def __str__(self):
        return self.designation

