from dataclasses import field
from django import forms
from .models import Attendance, AttendanceRegularization, Leave

LEAVE_CHOICES =(
    ('casual leave', 'Casual Leave'),
    ('loss of pay', 'Loss of Pay'),
    ('earned leave', 'Earned Leave'),
     ('sick leave', 'Sick Leave')
)
SHIFT_CHOICES = (
    ('morning', 'morning'),
    ('night', 'night')
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
    attachments = forms.FileField(label="Attachments (.pdf,.docx),size less than 2mb",widget=forms.FileInput(attrs={'class':'form-control'}),required = False)
    class Meta:
        model = Leave
        fields = ['leave_type','from_date','from_session','to_date','to_session','reason','attachments']


class AdminLeaveForm(forms.ModelForm):
    leave_type = forms.CharField(widget=forms.Select(choices=LEAVE_CHOICES,attrs = {'class':'form-control '}),required =True)
    from_session =  forms.CharField(widget= forms.Select(choices=SESSION_CHOICES ,attrs= {'class':'form-control '}),required =True)
    to_session =  forms.CharField(widget= forms.Select(attrs= {'class':'form-control'},choices=SESSION_CHOICES),initial='session 2',required =True)
    class Meta:
        model = Leave
        fields = ['leave_type','from_session','to_session']

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class RegularizeForm(forms.ModelForm):
    new_entry = forms.TimeField( label="New Entry Time",widget=TimePickerInput(attrs={'class':'form-control'}))
    new_exit = forms.TimeField(label="New Exit Time",widget=TimePickerInput(attrs={'class':'form-control'}))
    reason =  forms.CharField(label="Reason",widget=forms.Textarea(attrs={'class':'form-control','rows':1}))
    class Meta:
        model = AttendanceRegularization
        fields = ['new_entry','new_exit','reason']

class AdminAttendanceForm(forms.ModelForm):
    entry_time = forms.TimeField( label="Entry Time",widget=TimePickerInput(attrs={'class':'form-control'}))
    exit_time = forms.TimeField(label="Exit Time",widget=TimePickerInput(attrs={'class':'form-control'}))
    class Meta:
        model = Attendance
        fields = ['entry_time','exit_time']

class AdminEmpAttendance(forms.ModelForm):
    attendance_date = forms.DateField(widget=DateInput(attrs = {'class':'form-control '}),required=True)
    shift =  forms.CharField(widget= forms.Select(choices=SHIFT_CHOICES ,attrs= {'class':'form-control '}),required =True)
    entry_time = forms.TimeField( label="Entry Time",widget=TimePickerInput(attrs={'class':'form-control'}),required=True)
    exit_time = forms.TimeField(label="Exit Time",widget=TimePickerInput(attrs={'class':'form-control'}),required=True)

    class Meta:
        model = Attendance
        fields = ['attendance_date','shift','entry_time','exit_time']