from django import forms
from .models import Leave

LEAVE_CHOICES =(
    ('cl', 'Casual Leave'),
    ('lp', 'Loss of Pay'),
    ('el', 'Earned Leave'),
     ('sl', 'Sick Leave')
)

SESSION_CHOICES =(
    ('s1', 'Session 1'),
    ('s2', 'Session 2')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class LeaveForm(forms.ModelForm):
    leave_type = forms.CharField(widget=forms.Select(choices=LEAVE_CHOICES,attrs = {'class':'form-control '}),required =True)
    from_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    from_session =  forms.CharField(widget= forms.Select(choices=SESSION_CHOICES ,attrs= {'class':'form-control '}),required =True)
    to_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    to_session =  forms.CharField(widget= forms.Select(attrs= {'class':'form-control'},choices=SESSION_CHOICES),initial='s2',required =True)
    reason = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','rows':3}),required =True)
    class Meta:
        model = Leave
        fields = ['leave_type','from_date','from_session','to_date','to_session','reason']
