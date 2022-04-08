from admin.models import Payroll, Salary
from employees.models import Leave, LeaveCounter, YearCounter
import datetime
from django.db.models import Q

from users.models import Newuser


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

#to know how many days 
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



#if leave is multiple day (in admin side)
def calculate_leave(leave,date):
    if leave.from_date == date:
        if leave.from_session == 'session 1':
            return 1
        elif leave.from_session == 'session 2':
            return 0.5

    elif leave.to_date == date:
        if leave.to_session == 'session 2':
            return 1
        elif leave.to_session == 'session 1':
            return 0.5
    else:
        return 1

#if same day 
def same_day_number(leave):
    if leave.from_session == leave.to_session:
        return 0.5
    else:
         return 1     



#check if user have an approved leave
def leave_marked(emp,date):
    leaves = Leave.objects.filter(Q(from_date__month= date.month) | Q(to_date__month= date.month), user=emp).exclude(approval='rejected')
    if leaves:
        for leave in leaves:
            if leave.from_date != leave.to_date:
                day_count = (leave.to_date - leave.from_date).days + 1
                for single_date in (leave.from_date + datetime.timedelta(n) for n in range(day_count)):
                    if single_date == date:
                        return True
            else:
                if leave.from_date == date:
                    return True

def leave_approval(leave):
            if leave.from_date != leave.to_date:
                day_count = (leave.to_date - leave.from_date).days + 1
                for single_date in (leave.from_date + datetime.timedelta(n) for n in range(day_count)):
                    number = calculate_leave(leave,single_date) #get leave number in that day

                    month = single_date.month
                    count = LeaveCounter.objects.get(date__month=month,date__year=get_year(),user=leave.user)
                    count1 = YearCounter.objects.get(date__year=get_year(),user=leave.user)
                    if leave.leave_type == 'casual leave':
                        count.cl = count.cl + number
                        count1.cl = count1.cl + number
                    elif leave.leave_type == 'earned leave':
                        count.el = count.el + number
                        count1.el = count1.el + number
                    elif leave.leave_type == 'loss of pay':
                        count.lp = count.lp + number
                        count1.lp = count1.lp + number
                    elif leave.leave_type == 'sick leave':
                        count.sl = count.sl + number
                        count1.sl = count1.sl + number
                    count.save()
                    count1.save()


            else:
                number = same_day_number(leave)
                month = leave.from_date.month
                count = LeaveCounter.objects.get(date__month=month,date__year=get_year(),user=leave.user)
                count1 = YearCounter.objects.get(date__year=get_year(),user=leave.user)
                if leave.leave_type == 'casual leave':
                    count.cl = count.cl + number
                    count1.cl = count1.cl + number
                elif leave.leave_type == 'earned leave':
                    count.el = count.el + number
                    count1.el = count1.el + number
                elif leave.leave_type == 'loss of pay':
                    count.lp = count.lp + number
                    count1.lp = count1.lp + number
                elif leave.leave_type == 'sick leave':
                    count.sl = count.sl + number
                    count1.sl = count1.sl + number
                count.save()
                count1.save()

            leave.approval = 'approved'
            leave.save()



def leave_reject(leave):
            if leave.from_date != leave.to_date:
                day_count = (leave.to_date - leave.from_date).days + 1
                for single_date in (leave.from_date + datetime.timedelta(n) for n in range(day_count)):
                    number = calculate_leave(leave,single_date) #get leave number in that day

                    month = single_date.month
                    count = LeaveCounter.objects.get(date__month=month,date__year=get_year(),user=leave.user)
                    count1 = YearCounter.objects.get(date__year=get_year(),user=leave.user)
                    if leave.leave_type == 'casual leave':
                        count.cl = count.cl - number
                        count1.cl = count1.cl - number
                    elif leave.leave_type == 'earned leave':
                        count.el = count.el - number
                        count1.el = count1.el - number
                    elif leave.leave_type == 'loss of pay':
                        count.lp = count.lp - number
                        count1.lp = count1.lp - number
                    elif leave.leave_type == 'sick leave':
                        count.sl = count.sl - number
                        count1.sl = count1.sl - number
                    count.save()
                    count1.save()


            else:
                number = same_day_number(leave)
                month = leave.from_date.month
                count = LeaveCounter.objects.get(date__month=month,date__year=get_year(),user=leave.user)
                count1 = YearCounter.objects.get(date__year=get_year(),user=leave.user)
                if leave.leave_type == 'casual leave':
                    count.cl = count.cl - number
                    count1.cl = count1.cl - number
                elif leave.leave_type == 'earned leave':
                    count.el = count.el - number
                    count1.el = count1.el - number
                elif leave.leave_type == 'loss of pay':
                    count.lp = count.lp - number
                    count1.lp = count1.lp - number
                elif leave.leave_type == 'sick leave':
                    count.sl = count.sl - number
                    count1.sl = count1.sl - number
                count.save()
                count1.save()

            leave.approval = 'rejected'
            leave.save()
#calculate hra
def calc_hra(basic):
    hra = (40/100)*basic
    return hra

#calculate ta
def calc_ta(basic):
    ta = (20/100)*basic
    return ta

#calculate pf
def calc_pf(basic):
    pf = (12/100)*basic
    return pf

#calculate other benefits
def calc_ob(cdate,employee,basic):
    if cdate.month == 12:
        earnedleave = YearCounter.objects.get(date__year=cdate.year ,user=employee)
        if earnedleave.el < 12:
            single_day = basic/30
            left = 12 - earnedleave.el
            ob = left * single_day
    else:
        ob = 0
    return ob


#calculate other deductions
def calc_od(cdate,employee,basic):
    od = 0
    single_day = basic/30
    leave = LeaveCounter.objects.get(date__month = cdate.month,user=employee)
    if leave.sl > 0:
        pay = (single_day/2) * leave.sl
        od = od + pay
    if leave.lp > 0:
        pay = single_day * leave.lp
        od = od + pay
    return od

#calculate salary
def calculate_salary(cdate):
    employees = Newuser.objects.filter(is_employee=True)
    for employee in employees:
        hra = 0
        ta = 0
        pf = 0
        salary = Salary.objects.get(user=employee)
        basic = salary.basic_pay
        if salary.hra:
            hra = calc_hra(basic)
        if salary.ta:
            ta = calc_ta(basic)
        if salary.pf:
            pf = calc_pf(basic)
        ob = calc_ob(cdate,employee,basic)
        od = calc_od(cdate,employee,basic)
        net_salary = ((basic + hra + ta + ob)-pf) - od 
        Payroll.objects.create(basic = basic, hra = hra, ta = ta, pf = pf, other_benefits = ob, other_deductions = od, net_salary = net_salary, date = cdate, user = employee)   








