from django import forms
from .models import Leave

LEAVE_CHOICES =(
    ('casual leave', 'Casual Leave'),
    ('loss of pay', 'Loss of Pay'),
    ('earned leave', 'Earned Leave'),
     ('sick leave', 'Sick Leave')
)

SESSION_CHOICES =(
    ('session 1', 'Session 1'),
    ('session 2', 'Session 2')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class LeaveForm(forms.ModelForm):
    leave_type = forms.CharField(widget=forms.Select(choices=LEAVE_CHOICES,attrs = {'class':'form-control '}),required =True)
    from_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    from_session =  forms.CharField(widget= forms.Select(choices=SESSION_CHOICES ,attrs= {'class':'form-control '}),required =True)
    to_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    to_session =  forms.CharField(widget= forms.Select(attrs= {'class':'form-control'},choices=SESSION_CHOICES),initial='session 2',required =True)
    reason = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','rows':3}),required =True)
    class Meta:
        model = Leave
        fields = ['leave_type','from_date','from_session','to_date','to_session','reason']
