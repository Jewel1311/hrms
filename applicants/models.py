import datetime
from django.db import models
from django.forms import ValidationError
from base.models import Department, Jobs
from users.models import Newuser

class Applications(models.Model):
    applied_date = models.DateField(auto_now_add = True)
    selected = models.CharField(max_length=12,default='pending')
    user = models.ForeignKey(Newuser,on_delete=models.CASCADE )
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError("Date cannot be in the past")

class Interviews(models.Model):
    interview_date = models.DateField(validators=[validate_date])
    start_time = models.TimeField()
    end_time = models.TimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE) 
    description = models.TextField(default='')


class Messages(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()