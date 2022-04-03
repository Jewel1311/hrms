import datetime
from django import forms
from .models import Newuser
from django.contrib.auth.forms import UserCreationForm




class UserRegistrationForm(UserCreationForm):
        email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'form-control'}),required=True)
        first_name = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'}),required=True)
        middle_name = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'}),required=False)
        last_name = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'}),required=True)
            
        class Meta:
            model = Newuser
            fields = [ 'first_name','middle_name','last_name','email' ]


