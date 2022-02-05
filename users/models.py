from django.db import models
from django.forms import  ValidationError
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _


#custom manager Newuser
class CustomAccountManager(BaseUserManager):
    
   

    def create_user(self, email,middle_name, password, **other_fields):

        if not email:
            raise ValueError("You must provide an email address")

        email=self.normalize_email(email)
        user = self.model(email=email,middle_name=middle_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,middle_name,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Staff must be true")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be true")
                   
        return self.create_user(email,middle_name,password,**other_fields)


#creating the user
class Newuser(AbstractUser):
    username=None
    middle_name=models.CharField(max_length=60,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_applicant= models.BooleanField(default=False)
    is_employee= models.BooleanField(default=False)
    is_project_manager= models.BooleanField(default=False)
    

    objects=CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['middle_name']
    
    def __str__(self):
        return self.email


#profile for applicants

class ApplicantProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    user=models.OneToOneField(Newuser,unique=True,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=60)
    middle_name=models.CharField(max_length=30,blank=True,default='')
    last_name=models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob=models.DateField()
    place=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    pin=models.CharField(max_length=6)
    phone=models.CharField(max_length=10)
    cv=models.FileField()
    
    def __str__(self):
        return self.first_name

    



