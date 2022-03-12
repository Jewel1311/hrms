from django.db import models
from PIL import Image
from admin.models import Designations
from base.models import Department
from users.models import Newuser

class EmployeeProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    user=models.OneToOneField(Newuser,unique=True,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
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



class Leave(models.Model):
    leave_type = models.CharField(max_length=10)
    from_date = models.DateField()
    from_session = models.CharField(max_length=10)
    to_date = models.DateField()
    to_session = models.CharField(max_length=10)
    reason = models.TextField()
    user = models.ForeignKey(Newuser, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)

#to store the employees designation and department  
class EmployeeDesignation(models.Model):
    designation = models.ForeignKey(Designations, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(Newuser,on_delete=models.CASCADE)

 