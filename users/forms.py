from django import forms
from .models import Newuser
from django.contrib.auth.forms import UserCreationForm




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60,required=True)
    middle_name = forms.CharField(max_length=60,required=False)
    last_name = forms.CharField(max_length=60,required=True)
    class Meta:
        model = Newuser
        fields = [ 'first_name','middle_name','last_name','email' ]


