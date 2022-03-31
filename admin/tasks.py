from employees.models import LeaveCounter, YearCounter
import datetime


#returns the current year
def get_year():
    year = datetime.date.today().year
    return year
    
#returns the current month
def get_month():
    month = datetime.date.today().month
    return month

def get_balance(leave_form,user):
    leave = YearCounter.objects.get(date__year=get_year(),user=user)
    saved = leave_form.save(False)
    number = set_leave(saved)
    
    if leave_form.cleaned_data['leave_type'] == 'casual leave':
        if leave.cl + number >= 12:
            return True
        else:
            return False

    elif leave_form.cleaned_data['leave_type'] == 'earned leave':
        if leave.el + number >= 12:
            return True
        else:
            return False

    elif leave_form.cleaned_data['leave_type'] == 'sick_leave': 
        if leave.sl + number >= 15:
            return True
        else:
            return False

    else:
        return

# to set the yearly leave
def set_year_counter(leave):
    year = YearCounter.objects.get(date__year=get_year(),user=leave.user)
    leaves = LeaveCounter.objects.filter(date__year=get_year(),user=leave.user)  
    for leave in leaves:
        year.cl = year.cl + leave.cl
        year.el = year.el + leave.el
        year.lp = year.lp + leave.lp
        year.sl =year.sl + leave.sl


#return from date number if from date not equal to to date
def from_number(leave):
    if leave.from_session == 'session 1':
        return 1
    else:
        return 0.5

#return to date number if from date not equal to to date
def to_number(leave):
    if leave.to_session == 'session 2':
        return 1
    else:
        return 0.5


def set_leave(leave):
    if leave.from_date == leave.to_date:
        if leave.from_session == leave.to_session:
            return 0.5
        else:
            return 1
    else:
        f_no = from_number(leave)
        e_no = to_number(leave)
        if (leave.to_date - leave.from_date).days > 1:     #count number of days 
            diff = (leave.to_date - leave.from_date).days - 1
        else:
            diff = 0
        total =  f_no + e_no + diff
        return total