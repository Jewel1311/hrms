import datetime
from django.db import models
from PIL import Image
from django.forms import ValidationError
from django.urls import reverse
from admin.models import Designations
from base.models import Department
from users.models import Newuser

class EmployeeProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user=models.OneToOneField(Newuser,unique=True,on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField(null=True)
    addressline1 = models.CharField(max_length= 60,default='')
    place = models.CharField(max_length=60)
    city  =models.CharField(max_length=60)
    state = models.CharField(max_length=60) 
    pin = models.CharField(max_length=6) 
    phone = models.CharField( max_length=10) 
    photo = models.ImageField(default ='default/profile.png')


    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.photo.path)
        if image.height > 400 or image.width > 400:
            resize = (400,400)
            image.thumbnail(resize)
            image.save(self.photo.path)

class Attendance(models.Model):
    attendance_date = models.DateField()
    entry_time = models.TimeField(null=True)
    exit_time = models.TimeField(null=True)
    shift = models.CharField(max_length=10,default='')
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)

#to check if the date is a past date
def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError("Date cannot be in the past")

class Leave(models.Model):
    leave_type = models.CharField(max_length=20)
    from_date = models.DateField(validators=[validate_date])
    from_session = models.CharField(max_length=10)
    to_date = models.DateField(validators=[validate_date])
    to_session = models.CharField(max_length=10)
    reason = models.TextField()
    applied_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    approval = models.CharField(max_length=12,default='pending')

    def get_absolute_url(self):
        return reverse ("leave_detail",kwargs={"slug":self.id})

#to store the employees designation and department  
class EmployeeDesignation(models.Model):
    designation = models.ForeignKey(Designations, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(Newuser,on_delete=models.CASCADE)

 