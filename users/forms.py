
from dataclasses import fields
from email.policy import default
from tkinter import Widget
from django import forms
from .models import Newuser,ApplicantProfile
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60,required=True)
    middle_name = forms.CharField(max_length=60,required=False)
    last_name = forms.CharField(max_length=60,required=True)
    class Meta:
        model = Newuser
        fields = [ 'first_name','middle_name','last_name','email' ]

class Cv(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = ['cv']