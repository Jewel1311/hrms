import datetime 
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from admin.models import Designations
from base.models import Department

from employees.forms import LeaveForm
from .models import EmployeeDesignation, Leave
from .models import Attendance, EmployeeProfile
from django.contrib import messages


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
            return redirect('view_employee_profile')
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

      #to get designation of employee from EmployeeDesignation
      desig_obj = EmployeeDesignation.objects.get(user = request.user)
      designation = Designations.objects.get(id = desig_obj.designation_id )

      #to get department of employee from EmployeeDesignation

      dep_obj = EmployeeDesignation.objects.get(user = request.user)
      department = Department.objects.get(id = dep_obj.department_id )
      

      return render(request, "employees/viewemployeeprofile.html",{'employee':employee, 'designation':designation, 'department':department})
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
               morning_shift.shift = 'morning'
               morning_shift.user = request.user
               morning_shift.save()
               return redirect('morning_shift')

            elif 'exit' in request.POST:
               morning_shift = Attendance.objects.get(user = request.user, attendance_date = datetime.date.today(), shift = 'morning')
               morning_shift.exit_time = datetime.datetime.now().time()
               morning_shift.save()
               return redirect('morning_shift')
      else:                                                             
         try:
            #checks if an attendance object of the user for today exists

            check = Attendance.objects.get(user = request.user, attendance_date = datetime.date.today(), shift = 'morning') 

            #checks if the attendance is fully marked that is both fields are not none
            if check.entry_time is not None and check.exit_time is not None:
                  messages.success(request , f"You have marked todays attendance")
                  return render(request, 'employees/attendance.html',{'check':check,'shift':'morning' })
            else:
                  return render(request, 'employees/attendance.html', {'check':check,'shift':'morning'}) 
         except:
               check = Attendance()
               return render(request, 'employees/attendance.html', {'check':check,'shift':'morning'}) 


#mark night shift
@login_required
def night_shift(request):
      if request.method == "POST":
            if 'entry' in request.POST:
               night_shift = Attendance()
               night_shift.attendance_date = datetime.date.today()
               night_shift.entry_time = datetime.datetime.now().time()
               night_shift.shift = 'night'
               night_shift.user = request.user
               night_shift.save()
               return redirect('night_shift')

            elif 'exit' in request.POST:
               night_shift = Attendance.objects.get(user = request.user, attendance_date = datetime.date.today(), shift = 'night')
               night_shift.exit_time = datetime.datetime.now().time()
               night_shift.save()
               return redirect('night_shift')
      else:                                                             
         try:
            #checks if an attendance object of the user for today exists

            check = Attendance.objects.get(user = request.user, attendance_date = datetime.date.today(),shift = 'night') 

            #checks if the attendance is fully marked that is both fields are not none
            if check.entry_time is not None and check.exit_time is not None:
                  messages.success(request , f"You have marked your night shift")
                  return render(request, 'employees/attendance.html',{'check':check,'shift':'night'})
            else:
                  return render(request, 'employees/attendance.html', {'check':check,'shift':'night'}) 
         except:
               check = Attendance()
               return render(request, 'employees/attendance.html', {'check':check,'shift':'night'}) 
                 

     
#view attendance
@login_required
def attendance_view(request):
   if request.method == "POST":
      shift = request.POST['shift']
      attendance =  Attendance.objects.filter(user = request.user,shift = shift)
      return render(request, 'employees/attendance_view.html',{'attendance':attendance,'shift':shift})

   else:
      attendance =  Attendance.objects.filter(user = request.user,shift='morning')
      return render(request, 'employees/attendance_view.html',{'attendance':attendance})

#apply leave 
@login_required
def apply_leave(request):
   if request.method == "POST":
      leave_form = LeaveForm(request.POST)
      if leave_form.is_valid():
         print(leave_form.cleaned_data['leave_type'])
         leave = leave_form.save(False)
         leave.user = request.user
         leave.save()
         messages.success(request, f'Leave Applied')
      return redirect('apply_leave')
   else:  
      leave_form = LeaveForm()
      return render(request, 'employees/apply_leave.html',{ 'leave_form': leave_form })

# view leave
@login_required
def view_leave(request):
   leave = Leave.objects.filter(user = request.user).order_by('-id')
   return render(request,'employees/view_leave.html',{'leave':leave})