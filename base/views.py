import datetime
from admin.tasks import get_year
from django.shortcuts import render
from .models import Jobs
from users.models import Newuser
from employees.models import Attendance, LeaveCounter, YearCounter

def index(request):
     
     jobs = Jobs.objects.filter(withdraw_date__gte=datetime.date.today()).order_by('-posted_on')[:3]
     create_attendance()
     leave_counter()
     year_counter()
     return render(request, 'base/index.html',{'jobs':jobs})

# to create attendance column for everyday
def create_attendance():
     check = Attendance.objects.filter(attendance_date__gte=datetime.date.today()).count()
     if check == 0:
          employees = Newuser.objects.filter(is_employee = True)
          for employee in employees:
               Attendance.objects.create(attendance_date=datetime.date.today(),entry_time=None,exit_time=None,shift='morning',user=employee) 

# to update the leave counter every month
def leave_counter():
    check = LeaveCounter.objects.filter(date__year__gte=get_year()).count()
    if check == 0:
         year = get_year()
         i = 1
         while i<=12:
          date = datetime.date(year,i,1)
          employees = Newuser.objects.filter(is_employee = True)
          
          for employee in employees:
               LeaveCounter.objects.create(cl=0,el=0,lp=0,sl=0,date=date,user=employee)  
                      
          i = i+1

# to updat the leave counter every year
def year_counter():
    check = YearCounter.objects.filter(date__year__gte=get_year()).count()
    if check == 0:
          employees = Newuser.objects.filter(is_employee = True)
          for employee in employees:
               YearCounter.objects.create(cl=0,el=0,lp=0,sl=0,user=employee) 
                
