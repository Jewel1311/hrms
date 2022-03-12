from django import forms
from admin.models import Designations,Salary
from base.models import Department
from employees.models import  EmployeeDesignation
from users.forms import UserRegistrationForm
from users.models import Newuser


# add employee registration details

class AddEmployeeForm(UserRegistrationForm):
    password1 = forms.CharField(
            label="Password",
            widget=forms.PasswordInput(attrs={'class':'form-control'},),required=True)
    password2 = forms.CharField(
            label="Confirm password",
            widget=forms.PasswordInput(attrs={'class':'form-control'},),required=True)
            
    class Meta:
            model = Newuser
            fields = [ 'first_name','middle_name','last_name','email']


# add employee salary details

class SalaryForm(forms.ModelForm):
    basic_pay = forms.IntegerField(widget=forms.TextInput(attrs= {'class':'form-control'}),required=True)
    hra = forms.BooleanField(widget= forms.CheckboxInput(attrs= {'class':'form-control'}),required=False)
    ta = forms.BooleanField(widget= forms.CheckboxInput(attrs= {'class':'form-control'}),required=False)
    pf = forms.BooleanField(widget= forms.CheckboxInput(attrs= {'class':'form-control'}),required=False)
    class Meta:
        model = Salary
        fields = ['basic_pay','hra','ta','pf']
    
class DesignationForm(forms.ModelForm):
    designation = forms.ModelChoiceField(Designations.objects.all(),widget=forms.Select(attrs= {'class':'form-control'}),required=True)
    department = forms.ModelChoiceField(Department.objects.all(),widget=forms.Select(attrs= {'class':'form-control'}),required=True)

    class Meta:
        model = EmployeeDesignation
        fields = ['designation','department']