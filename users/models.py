from django.db import models
from django.forms import  ValidationError
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator



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
  
    

    objects=CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['middle_name']


    # override the save method of Newuser
    
    # def save(self,*args, **kwargs):
    #     super().save(False)                   # saves the current created user
    #     if not self.is_superuser:
    #         inst_check = ApplicantProfile.objects.filter(user=self.id).count()  # check whether a profile of current user exists


    #         if inst_check:                          
    #             applicant_ins= ApplicantProfile.objects.get(user=self.id)    # if user exists take that existing instance(row)

    #         else:     
    #             applicant_ins = ApplicantProfile()    # else create an instance of Applciant Profile

    #             applicant_ins.user = self             # connects the two tables ,primary key of the user table with foreign key 
    #                                                 # of Applicnt profile(here 'user' is the forign key)

    #         applicant_ins.first_name=self.first_name      #insert the values
    #         applicant_ins.middle_name=self.middle_name   
    #         applicant_ins.last_name=self.last_name
    #         applicant_ins.save()                           #save the Applicant Profile instance

    #     super().save(*args, **kwargs)                  # save the user
    

    def __str__(self):
        return self.email
#profile for applicants

class ApplicantProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Nil', 'Nil'),
    )
    user=models.OneToOneField(Newuser,unique=True,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob=models.DateField(null=True)
    addressline1 = models.CharField(max_length= 60,default='')
    place=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    last_apply = models.DateField(null=True)
    pin = models.CharField( max_length=6) 
    phone = models.CharField( max_length=10) 
    cv=models.FileField()
    
    
    



