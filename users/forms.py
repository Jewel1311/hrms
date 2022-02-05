
from tkinter import Widget
from django import forms
from .models import Newuser
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    middle_name = forms.CharField(max_length=60)
    class Meta:
        model = Newuser
        fields = [ 'first_name','middle_name','last_name','email','password' ]

        Widgets = {
            'first_name':forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name':forms.TextInput(attrs = {'class': 'form-control'}),
            'middle_name':forms.TextInput(attrs = {'class': 'form-control'}),
            'email':forms.TextInput(attrs = {'class': 'form-control'}),
            'password':forms.PasswordInput(attrs = {'class': 'form-control'}),

        }

