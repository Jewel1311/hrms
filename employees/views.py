import datetime 
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pymysql import NULL
from .models import Attendance, EmployeeProfile
from django.contrib import messages
from django.db.models import Q

@login_required
def employee_home(request):
   employee = EmployeeProfile.objects.get(user = request.user)
   return render(request, 'employees/employee-home.html',{'employee':employee})

@login_required
def employee_profile(request):
   profile = EmployeeProfile.objects.filter(user = request.user).count() #check if profile for user exists or not
   if profile:
      employee = EmployeeProfile.objects.get(user = request.user)
   if request.method == "POST":
         addressline1 = request.POST['addressline1']
         place = request.POST['place']
         city = request.POST['city']
         state = request.POST['state']
         mobile = request.POST['mobile']
         pin = request.POST['pin']
         dob = request.POST['dob']
         gender = request.POST['gender']
         
         if request.FILES: 
            photo = request.FILES['photo']
            print(mobile)

         if len(mobile)!=10:
            messages.warning(request, f'Phone number must be 10 digits')
            if profile:
               return render(request, "employees/employeedetails.html",{'employee':employee})
            else:
               return render(request, 'employees/employeedetails.html')
         elif len(pin) != 6:
            messages.warning(request, f'Postcode must be 6 digits')
            if profile:
               return render(request, "employees/employeedetails.html",{'employee':employee})
            else:
               return render(request, 'employees/employeedetails.html')
         else: 
            if not profile:
               employee = EmployeeProfile()
               employee.user = request.user

            employee.addressline1 = addressline1
            employee.place = place
            employee.city = city
            employee.state = state
            employee.phone = mobile
            employee.pin = pin
            employee.dob = dob
            employee.gender = gender                      
            if request.FILES:
               employee.photo = photo
            employee.save()
            return redirect('filterlogin')
   else:                                                          #render the form if not post request 
      if profile:
         employee = EmployeeProfile.objects.get(user = request.user)
         return render(request, "employees/employeedetails.html",{'employee':employee}) 
      else:
         return render(request, 'employees/employeedetails.html')


@login_required 
def view_employee_profile(request):
   profile = EmployeeProfile.objects.filter(user = request.user).count()
   if profile:
      employee = EmployeeProfile.objects.get(user = request.user)
      return render(request, "employees/viewemployeeprofile.html",{'employee':employee})
   else:    
      return redirect('filterlogin')


# Employee Attendance

@login_required
def morning_shift(request):
      if request.method == "POST":
            if 'entry' in request.POST:
               morning_shift = Attendance()
               morning_shift.attendance_date = datetime.date.today()
               morning_shift.entry_time = datetime.datetime.now().time()
               morning_shift.user = request.user
               morning_shift.save()
               return redirect('morning_shift')

            elif 'exit' in request.POST:
               morning_shift = Attendance.objects.filter(user = request.user).filter(attendance_date = datetime.date.today())
               morning_shift.exit_time = datetime.datetime.now().time()
               morning_shift.save()
               return redirect('morning_shift')
      else:
            check = Attendance.objects.filter(user = request.user).filter(attendance_date = datetime.date.today())
            if check:
               if check.entry_time is not None and check.exit_time is not None:
                  messages.warning(request , f"You have marked todays attendance")
                  return render(request, 'employees/morningshift.html')
               else:
                  return render(request, 'employees/morningshift.html', {'check':check}) 
            else:
               check = Attendance()
               return render(request, 'employees/morningshift.html', {'check':check}) 

                 

     
