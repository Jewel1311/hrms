from unicodedata import category
from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Department'


    def __str__(self):
        return self.department_name


class Jobs(models.Model):
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    skills = models.TextField(default='')
    location = models.CharField(max_length=60)
    posted_on = models.DateField(auto_now_add=True)
    withdraw_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Jobs'


    def __str__(self):
        return self.job_title