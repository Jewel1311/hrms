import datetime
from pyexpat import model
from django.db import models
from django.forms import ValidationError
from django.urls import reverse



class Department(models.Model):
    department_name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Department'


    def __str__(self):
        return self.department_name

#to check if the date is a past date
def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError("Date cannot be in the past")
        
class Jobs(models.Model):
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    skills = models.TextField(default='')
    location = models.CharField(max_length=60)
    posted_on = models.DateField(auto_now_add=True)
    withdraw_date = models.DateField(validators=[validate_date])
    salary = models.BigIntegerField(null=True)
    scheduled = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Jobs'

    def get_absolute_url(self):
        return reverse ("job_detail_view",kwargs={"slug":self.id})
        
    def __str__(self):
        return self.job_title