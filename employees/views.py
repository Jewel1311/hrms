from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

import employees
from .models import EmployeeProfile
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
