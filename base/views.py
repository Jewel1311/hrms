import datetime
from admin.tasks import get_month,get_year
from django.shortcuts import render
from .models import Jobs
from users.models import Newuser
from employees.models import LeaveCounter

def index(request):
     
     jobs = Jobs.objects.filter(withdraw_date__gte=datetime.date.today()).order_by('-posted_on')[:3]
     leave_counter()
     return render(request, 'base/index.html',{'jobs':jobs})

# to update the leave counter every month
def leave_counter():
    check = LeaveCounter.objects.filter(date__month__gte=get_month(),date__year__gte=get_year()).count()
    if check == 0:
          employees = Newuser.objects.filter(is_employee = True)
          for employee in employees:
               LeaveCounter.objects.create(cl=0,el=0,lp=0,sl=0,user=employee)   