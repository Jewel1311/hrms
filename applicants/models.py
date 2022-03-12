from operator import mod
from django.db import models
from base.models import Department, Jobs
from users.models import Newuser

class Applications(models.Model):
    applied_date = models.DateField(auto_now_add = True)
    selected = models.BooleanField(default=False)
    user = models.ForeignKey(Newuser,on_delete=models.CASCADE )
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)


class Interviews(models.Model):
    interview_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE) 
    description = models.TextField(default='')
    