from email.message import Message
from django import forms
from admin.models import Designations, Holidays, Payroll,Salary
from applicants.models import Interviews, Messages, Messages
from base.models import Department
from employees.models import  EmployeeDesignation
from users.forms import UserRegistrationForm
from users.models import Newuser
from base.models import Jobs

LOCATION_CHOICES =(
    ('Kochi,Kerala', 'Kochi,Kerala'),
)
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

class EditEmployeeForm(forms.ModelForm): 
        class Meta:
            model = Newuser
            fields = [ 'first_name','middle_name','last_name','email']
        

# add employee salary details

class SalaryForm(forms.ModelForm):
    basic_pay = forms.IntegerField(widget=forms.TextInput(attrs= {'class':'form-control'}),required=True)
    hra = forms.BooleanField(widget= forms.CheckboxInput(attrs= {'class':'form-check-inline'}),required=False)
    ta = forms.BooleanField(widget= forms.CheckboxInput(attrs= {'class':'form-check-inline'}),required=False)
    pf = forms.BooleanField(widget= forms.CheckboxInput(attrs= {'class':'form-check-inline'}),required=False)
    class Meta:
        model = Salary
        fields = ['basic_pay','hra','ta','pf']

# to add designation and department of employee  
class DesignationForm(forms.ModelForm):
    designation = forms.ModelChoiceField(Designations.objects.all(),widget=forms.Select(attrs= {'class':'form-control'}),required=True)
    department = forms.ModelChoiceField(Department.objects.all(),widget=forms.Select(attrs= {'class':'form-control'}),required=True)

    class Meta:
        model = EmployeeDesignation
        fields = ['designation','department']

class DateInput(forms.DateInput):
    input_type = 'date'

# to add jobs 

class JobForm(forms.ModelForm):
        job_title = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control '}),required =True)
        job_description = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control','rows':4}),required=True)
        location =  forms.CharField(widget= forms.Select(choices=LOCATION_CHOICES ,attrs= {'class':'form-control '}),required =True)
        withdraw_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
        skills = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','rows':4}),required =True)
        salary = forms.IntegerField(widget= forms.NumberInput(attrs={'class':'form-control'}),required =True)
        department = forms.ModelChoiceField(Department.objects.all(),widget=forms.Select(attrs= {'class':'form-control'}),required=True)
        class Meta:
                model = Jobs
                fields = ['job_title','job_description','location','withdraw_date','skills','salary','department']




class TimePickerInput(forms.TimeInput):
        input_type = 'time'

#interview form

class InterviewForm(forms.ModelForm):
    interview_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    start_time =  forms.TimeField(widget=TimePickerInput(attrs={'class':'form-control'}),required=True)
    end_time = forms.TimeField(widget=TimePickerInput(attrs={'class':'form-control'}),required=True)
    description = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','rows':4}),required =True)
    class Meta:
        model = Interviews
        fields = ['interview_date','start_time','end_time','description']


class MessageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control '}),required =True)
    body = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control','rows':4}),required=True)

    class Meta:
        model = Messages
        fields = ['title','body']


class PayrollEditForm(forms.ModelForm):
    other_benefits= forms.CharField(label="Add Benfits",widget=forms.NumberInput(attrs = {'class':'form-control '}),initial=0,required =True)
    other_deductions= forms.CharField(label="Add Deductions",widget=forms.NumberInput(attrs = {'class':'form-control'}),initial=0,required=True)

    class Meta:
        model = Payroll
        fields = ['other_benefits','other_deductions']

class HolidayForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    reason = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','rows':2}),required =True)
    class Meta:
        model = Holidays
        fields = ['date','reason']