from employees.models import LeaveCounter
import datetime


#returns the current year
def get_year():
    year = datetime.date.today().year
    return year
    
#returns the current month
def get_month():
    month = datetime.date.today().month
    return month

def get_balance(leave_type,user):
    cl=0
    el=0
    sl=0
    leave = LeaveCounter.objects.filter(date__year=get_year(),user=user)
    if leave_type == 'casual leave':
        for leave in leave:
            cl = cl + leave.cl
        if cl >= 12:
            return True
        else:
            return False

    elif leave_type == 'earned leave':
        for leave in leave:
            el = el + leave.el
        if el >= 12:
            return True
        else:
            return False

    elif leave_type == 'sick_leave':
        for leave in leave:
            sl = sl + leave.sl
        
        if el >= 15:
            return True
        else:
            return False

    else:
        return

# to take the yearly leave
def counter(leave):
    cl=0
    el=0
    lp=0
    sl=0
    leave = LeaveCounter.objects.filter(date__year=get_year(),user=leave.user)  
    for leave in leave:
        cl = cl + leave.cl
        el = el + leave.el
        lp = lp + leave.lp
        sl = sl + leave.sl
    year_counter=[cl,el,lp,sl]
    return year_counter

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