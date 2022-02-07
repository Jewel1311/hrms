from unicodedata import category
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Category'


    def __str__(self):
        return self.category


class Jobs(models.Model):
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    location = models.CharField(max_length=60)
    posted_on = models.DateField(auto_now_add=True)
    withdraw_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Jobs'


    def __str__(self):
        return self.job_title