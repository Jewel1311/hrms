import datetime
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from admin.models import Designations
from admin.tasks import get_balance
from applicants.models import Messages
from base.models import Department
from employees.forms import LeaveForm, RegularizeForm
from .models import AttendanceRegularization, EmployeeDesignation, Leave
from .models import Attendance, EmployeeProfile
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.views import PasswordChangeView


class MyPasswordChangeView(SuccessMessageMixin,PasswordChangeView):
   template_name = 'employees/change_password.html'
   success_message = "Password Changed"
   success_url = reverse_lazy('employee-password-change')


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
               morning_shift = Attendance.objects.get(user=request.user,attendance_date=datetime.date.today())
               morning_shift.entry_time = datetime.datetime.now().time()
               morning_shift.shift = 'morning'
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
      attendance =  Attendance.objects.filter(user = request.user,shift = shift).order_by('-attendance_date')
      return render(request, 'employees/attendance_view.html',{'attendance':attendance,'shift':shift})

   else:
      attendance =  Attendance.objects.filter(user = request.user,shift='morning').order_by('-attendance_date')
      return render(request, 'employees/attendance_view.html',{'attendance':attendance})

#apply leave 
@login_required
def apply_leave(request):
   if request.method == "POST":
      leave_form = LeaveForm(request.POST, request.FILES)
      if leave_form.is_valid():

         if request.FILES:
            file = request.FILES['attachments']
            if file.size > 2000000:
               messages.warning(request, f'File size should be less than 2 mb')
               return render(request, 'employees/apply_leave.html',{ 'form': leave_form }) 

         #leave balance check
         balance = get_balance(leave_form,request.user)
         leave_type = leave_form.cleaned_data['leave_type']
         if balance:
            messages.warning(request, f'Please check your {leave_type.upper()} availability')
            return render(request, 'employees/apply_leave.html',{ 'form': leave_form }) 

         leave = leave_form.save(False)
         leave.user = request.user
         leave.save()
         messages.success(request, f'Leave Applied') 
         return redirect('view_leave')  
      else:
         return render(request, 'employees/apply_leave.html',{ 'form': leave_form })
   else:  
      form = LeaveForm()
      return render(request, 'employees/apply_leave.html',{ 'form': form })

# view leave
@login_required
def view_leave(request):
   leaves = Leave.objects.filter(user = request.user).order_by('-id')
   return render(request,'employees/view_leave.html',{'leaves':leaves })

#to get the detail view of attendance 

@login_required
def leave_detail(request,slug):
    leave = Leave.objects.get(id = slug)
    return render(request, 'employees/leave_detail.html',{ 'leave':leave })

#edit leave 
class EditLeave(SuccessMessageMixin,UpdateView):
   model = Leave
   form_class = LeaveForm
   template_name = 'employees/apply_leave.html'
   success_message = "Leave Updated"

#to get id of selected attendance
@login_required
def selected_attendance(request):
   if request.method == "POST":
      id = request.POST['regularize']
      if id:
         return redirect('attendance_regularization', pk=id)
      else:
         messages.warning(request, f'Select an attendance to regularize')
         return redirect('attendance_view')


#to regularize   
@login_required
def attendance_regularization(request,pk):  
   form = RegularizeForm()
   attendance = Attendance.objects.get(id = pk)
   context = {
         'attendance':attendance,
         'form' :form
   }
   if request.method == "POST":
      reg_form = RegularizeForm(request.POST)
      if reg_form.is_valid():
         regulization = reg_form.save(False)
         regulization.date = attendance.attendance_date
         regulization.old_entry = attendance.entry_time
         regulization.old_exit = attendance.exit_time
         regulization.shift = attendance.shift
         regulization.user = request.user
         regulization.attendance = attendance
         regulization.save()
         messages.success(request,f'Regulization Requested')
         return redirect('regularization_requests')
      else:
         return render(request,'employees/attendance_regularization.html',context)

   else:
      return render(request,'employees/attendance_regularization.html',context)

#to view the regulization requests
@login_required
def regularization_requests(request):
   requests = AttendanceRegularization.objects.filter(user = request.user).order_by('-id')
   print(requests)
   context = {
      'requests':requests,
   }
   return render(request,'employees/regularization_requests.html',context)


#view notifications
@login_required
def view_notification(request):
   message = Messages.objects.filter(date__gte = request.user.date_joined).order_by('-id')
   count = Messages.objects.filter(date__gte = request.user.date_joined).count()
   context = {
        'message':message,
        'count':count,
   }
   if request.method == "POST":
            value = request.POST['search_msg']
            message = Messages.objects.filter(Q (title__icontains=value) | Q(date__icontains=value)).filter(date__gte = request.user.date_joined).order_by('-id')
            c = message.count()
            if c == 0:
                messages.info(request,f'No results found')
                return redirect('view_notification')
            else:
               p = Paginator(message,5)  # second argument is no of items to be displayed
               page_num = request.GET.get('page',1 ) #get the page no by url  and 1 is default
               try:
                  page = p.page(page_num)
               except EmptyPage:
                  page = p.page(1)
               return render(request, 'employees/view_notification.html',{'message':page,'count':count})

   else:
      if count != 0:
            p = Paginator(message,5)  # second argument is no of items to be displayed
            page_num = request.GET.get('page',1 ) #get the page no by url  and 1 is default
            try:
               page = p.page(page_num)
            except EmptyPage:
               page = p.page(1)
            return render(request, 'employees/view_notification.html',{'message':page,'count':count})
      else:
            return render(request, 'employees/view_notification.html',context)
   

#detail view of messages
@login_required
def notification_detail(request,pk):
    message = Messages.objects.get(id=pk)
    return render(request, 'employees/notification_details.html',{'message':message})
      