import datetime
from multiprocessing import context
from employees.forms import AdminAttendanceForm, AdminEmpAttendance, AdminLeaveForm, AdminRegularizationForm
from .tasks import calculate_salary, get_balance, get_month,get_year, leave_approval, leave_marked, leave_reject
from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from admin.forms import AddEmployeeForm, DesignationForm, EditEmployeeForm, HolidayForm, InterviewForm, JobForm, MessageForm, PayrollEditForm, SalaryForm
from django.contrib import messages
from admin.models import Designations, Holidays, Payroll, Salary
from applicants.models import Applications, Interviews, Messages
from base.models import Department, Jobs
from employees.models import Attendance, AttendanceRegularization, EmployeeDesignation, Leave, LeaveCounter, YearCounter
from users.models import ApplicantProfile, Newuser
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.views import PasswordChangeView

@login_required
def admin_home(request):
    employees = Newuser.objects.filter(is_employee=True).count()
    applicants = Newuser.objects.filter(is_applicant=True).count()
    department = Department.objects.all().count()
    designations = Designations.objects.all().count()
    interviews = Interviews.objects.filter(interview_date__gt=datetime.date.today()).count()
    leave_count = Leave.objects.filter(approval = 'pending').count()
    leaves = Leave.objects.filter().order_by('-id')[:3]
    regular_count = AttendanceRegularization.objects.filter(status='pending').count()
    regular = AttendanceRegularization.objects.filter().order_by('-id')[:3]
    att_count = Attendance.objects.filter(attendance_date = datetime.date.today(),shift='morning').exclude(entry_time = None).count()
    mon_leave = Leave.objects.filter(applied_date__month = datetime.date.today().month,applied_date__year=datetime.date.today().year).count()
    mon_app = Leave.objects.filter(applied_date__month = datetime.date.today().month,applied_date__year=datetime.date.today().year,approval='approved').count()
    att_per = int((att_count/employees)*100)
    reg_mon = AttendanceRegularization.objects.filter(date__month=datetime.date.today().month,date__year=datetime.date.today().year).count()
    reg_app = AttendanceRegularization.objects.filter(date__month=datetime.date.today().month,date__year=datetime.date.today().year,status='approved').count()
    up_int = Interviews.objects.filter(interview_date__gt=datetime.date.today()).order_by('interview_date').first()
    holiday = Holidays.objects.filter(date__gt = datetime.date.today()).order_by('date').first()
    jobs = Jobs.objects.filter().order_by('-id')[:2]
    job_count = Jobs.objects.all().count()
    context = {
       'employees':employees,
       'applicants':applicants,
       'department':department,
       'designations':designations,
       'interviews':interviews,
       'leave_count':leave_count,
       'leaves':leaves,
       'regular_count':regular_count,
       'regular':regular,
       'att_per':att_per,
       'att_count':att_count,
       'mon_leave':mon_leave,
       'mon_app':mon_app,
       'reg_mon':reg_mon,
       'reg_app':reg_app,
       'up_int':up_int,
       'holiday':holiday,
       'jobs':jobs,
       'job_count':job_count


    }
    return render(request, 'admin/admin_dashboard.html',context)


class AdPasswordChangeView(SuccessMessageMixin,PasswordChangeView):
   template_name = 'admin/admin_password_change.html'
   success_message = "Password Changed"
   success_url = reverse_lazy('admin_password_change')

# adding the employee

@login_required
def add_employee(request):
    if request.method == "POST":
        reg_form = AddEmployeeForm(request.POST)    #containes detials for newuser table
        salary_form = SalaryForm(request.POST)      #contines details for salary table
        desig_form = DesignationForm(request.POST)  #contains details for EmployeeDesignation table


        if reg_form.is_valid() and salary_form.is_valid() and desig_form.is_valid():
            user = reg_form.save(False)
            user.is_employee = True
            user.save()

            salary = salary_form.save(False)
            salary.user = user

            designation = desig_form.save(False)
            designation.user =user 

           #to create month counter
            year = get_year()
            i = 1
            while i<=12:
                date = datetime.date(year,i,1)
                LeaveCounter.objects.create(cl=0,el=0,lp=0,sl=0,date=date,user=user)       
                i = i+1

            #to create year
            YearCounter.objects.create(cl=0,el=0,lp=0,sl=0,user=user) 

            #to create the attendance for that day
            Attendance.objects.create(attendance_date=datetime.date.today(),entry_time=None,exit_time=None,shift='morning',user=user)

            salary.save()
            designation.save()


            messages.success(request,f'Employee added')
            reg_form = AddEmployeeForm()
            salary_form = SalaryForm()
            desig_form = DesignationForm()
            return render(request, 'admin/add-employee.html', {'reg_form':reg_form, 'salary_form':salary_form, 'desig_form':desig_form })
        
        else:
            
            return render(request, 'admin/add-employee.html', {'reg_form':reg_form, 'salary_form':salary_form, 'desig_form':desig_form })
            
    
    else:
        reg_form = AddEmployeeForm()
        salary_form = SalaryForm()
        desig_form = DesignationForm()
        return render(request, 'admin/add-employee.html', {'reg_form':reg_form, 'salary_form':salary_form, 'desig_form':desig_form })

# view the employees in table 
@login_required
def view_employee(request):
    employees = Newuser.objects.filter(is_employee = True).order_by('first_name')
    obj = EmployeeDesignation.objects.all()
    
    return render(request, 'admin/employee-view.html',{'employees':employees,'obj':obj})

#detailed view of an employee
@login_required
def employee_detail(request,pk):
    employee = Newuser.objects.get(id = pk)
    #to get designation of employee from EmployeeDesignation
    desig_obj = EmployeeDesignation.objects.get(user = pk)
    designation = Designations.objects.get(id = desig_obj.designation_id )

    #to get department of employee from EmployeeDesignation

    dep_obj = EmployeeDesignation.objects.get(user = pk)
    department = Department.objects.get(id = dep_obj.department_id )

    salary = Salary.objects.get(user = pk)  
    
    return render(request, 'admin/employee-detail.html',{ 'employee':employee, 'designation':designation, 'department':department,'salary':salary})

#edit employee 
@login_required
def employee_edit(request,pk):

    #get the instance that we are updateing currently
    emp = Newuser.objects.get(id = pk)
    sal = Salary.objects.get(user = pk)
    desig = EmployeeDesignation.objects.get(user = pk)

    if request.method == "POST":
        employee = EditEmployeeForm(request.POST, instance=emp)
        salary = SalaryForm(request.POST,instance=sal)
        designation = DesignationForm(request.POST,instance=desig)

        if employee.is_valid() and salary.is_valid() and designation.is_valid():
            employee.save()
            salary.save()
            designation.save()
            messages.success(request,f'Changes Saved for the Employee')
            return redirect(employee_detail,pk)
        else:
            return redirect(employee_detail,pk)

    else:    

        reg_form = EditEmployeeForm(instance = emp)
        salary_form = SalaryForm(instance = sal)
        desig_form = DesignationForm(instance=desig)

        return render(request, 'admin/edit_employee.html', {'reg_form':reg_form, 'salary_form':salary_form, 'desig_form':desig_form })
    

#  Delete an employee 
@login_required
def delete_employee(requset,pk):
    employee = Newuser.objects.get(id=pk)
    employee.delete()
    messages.success(requset,f'Employee Deleted')
    return redirect('view_employee')

# department 
@login_required
def department(request):
    if request.method == "POST":
        department = Department()
        department.department_name = request.POST['department']
        department.save()
        messages.success(request,f'Department Added')
        return redirect('department')
    else:
        departments = Department.objects.all()
        return render(request, 'admin/department-view.html',{'departments':departments})

# Designations 
@login_required
def designations(request):
    if request.method == "POST":
        designation = Designations()
        designation.designation = request.POST['designation']
        designation.save()
        messages.success(request,f'Designation Added')
        return redirect('designations')
    else:
        designations = Designations.objects.all()
        return render(request, 'admin/designation.html',{'designations':designations})

# Edit Designation 
@login_required
def designation_edit(request,pk):
    if request.method == "POST":
        designation = Designations(id = pk)
        designation.designation = request.POST['designation']
        designation.save()
        messages.success(request,f'Designation Updated')
        return redirect('designations')
    else:
        edit = Designations.objects.get(id = pk)
        return render(request, 'admin/designation_edit.html',{'edit': edit})

# Edit Department 
@login_required
def department_edit(request,pk):
    if request.method == "POST":
        department = Department(id = pk)
        department.department_name = request.POST['department']
        department.save()
        messages.success(request,f'Department Updated')
        return redirect('department')
    else:
        edit = Department.objects.get(id = pk)
        return render(request, 'admin/department_edit.html',{'edit': edit})

# delete Department
class DeleteDepartment(SuccessMessageMixin,DeleteView):
    template_name = 'admin/department_delete.html'
    success_message = "Department Deleted"
    success_url = reverse_lazy('department')

    def get_object(self):
        id =  self.kwargs.get("pk")
        # print(id)
        return get_object_or_404(Department, id=id)
   

# delete Designation
class DeleteDesignation(SuccessMessageMixin,DeleteView):
    template_name = 'admin/designation_delete.html'
    success_message = "Designation Deleted"
    success_url = reverse_lazy('designations')

    def get_object(self):
        id =  self.kwargs.get("pk")
        print(id)
        return get_object_or_404(Designations, id=id)
   
# job add for applicant 
@login_required
def add_jobs(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Job Added')
            return redirect('add_jobs')
        else:
            return render(request, 'admin/add_jobs.html',{'form':form })
    else:    
        form = JobForm() 
        return render(request, 'admin/add_jobs.html',{'form':form })

# view all the jobs
@login_required
def view_all_jobs(request):
    jobs = Jobs.objects.all()
    return render(request, 'admin/view_jobs.html',{ 'jobs':jobs })

#detailed job view
@login_required
def job_detail_view(request,slug):
    job_id = Jobs.objects.get(id = slug)
    return render(request, 'admin/admin_jobdetail_view.html',{'job_id': job_id})

#edit Job
class EditJob(SuccessMessageMixin,UpdateView):
   model = Jobs
   form_class = JobForm
   template_name = 'admin/add_jobs.html'
   success_message = "Job Updated"

#delete job by admin
@login_required
def delete_job(request,pk):
    job = Jobs.objects.get(id=pk)
    job.delete()
    messages.success(request,f'Job Deleted')
    return redirect('view_all_jobs')

#view applicants by admin
@login_required
def view_applicants(request):
    applicants = Newuser.objects.filter(is_applicant=True)
    return render(request,'admin/view_applicants.html',{ 'applicants':applicants})

#view applicant details
@login_required
def applicant_details(request,pk):
    applicant = ApplicantProfile.objects.get(user=pk)
    return render(request, 'admin/view_applicant_details.html',{'applicant':applicant})

#  Delete an applicant
@login_required
def delete_applicants(requset,pk):
    applicant = Newuser.objects.get(id=pk)
    applicant.delete()
    messages.success(requset,f'Applicant Deleted')
    return redirect('view_applicants')

@login_required
def applications(request,pk):
    applications = Applications.objects.filter(job = pk).order_by('-applied_date')
    job = Jobs.objects.get(id = pk)
    context = {
        'applications':applications,
        'job':job
    }
    return render(request, 'admin/view_applications.html',context)

#to accept the applicant 
@login_required
def applicant_status(request,id,jobid,btn):
    applicant = Applications.objects.get(id = id)
    user = applicant.user.first_name +' '+ applicant.user.middle_name +' '+ applicant.user.last_name 
    if btn == 'accept':
        applicant.selected = 'accepted'
        messages.success(request,f'{user} Accepted')
    elif btn == 'reject':
        applicant.selected = 'rejected'
        messages.warning(request,f'{user} Rejected')
    applicant.save()
    return redirect('applications', pk= jobid)

#to check if any interview is ready to be scheduled
@login_required
def check_schedule(request):
    jobs = Jobs.objects.filter(withdraw_date__lt=datetime.date.today()).order_by('-withdraw_date')
    context = {
        'jobs':jobs
    }
    return render(request,'admin/check_schedule.html',context)


#scheule interview
@login_required
def add_interview(request,pk):
    job = Jobs.objects.get(id=pk)
    if request.method =="POST": 
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(False)
            interview.job = job
            interview.department = job.department
            job.scheduled = True
            job.save()
            interview.save()
            messages.success(request,f'Interview added')
            return redirect('check_schedule')
        else:
            return render(request,'admin/add_interview.html',{'form':form,'job':job})
    else:
        form = InterviewForm()
        return render(request,'admin/add_interview.html',{'form':form,'job':job})

#view scheduled interviews
@login_required
def scheduled_interviews(request,pk):
    interview = Interviews.objects.get(job=pk)
    return render(request,'admin/view_scheduled_interviews.html',{'interview':interview})

#edit scheduled interviews 
@login_required
def edit_interviews(request,pk):
    interview = Interviews.objects.get(job=pk)  #take the interview with the given job id
    job = Jobs.objects.get(id =pk)  #get job to display job title in template
    if request.method == "POST":
        form = InterviewForm(request.POST,instance=interview) 
        if form.is_valid():
            form.save()
            messages.success(request,f'Interview Edited')
            return redirect('scheduled_interviews',pk=pk)
        else:
            return render(request,'admin/add_interview.html',{'form':form,'job':job})
        
    else:
        form = InterviewForm(instance=interview)
        return render(request,'admin/add_interview.html',{'form':form,'job':job})

@login_required
def selected_applicants(request,pk):
    applications = Applications.objects.filter(job = pk, selected ='accepted')
    return render(request, 'admin/view_selected_applicants.html',{'applications':applications})

#cancel a scheduled interview
@login_required 
def cancel_interview(request,pk):
    if request.method == "POST":
        interview = Interviews.objects.get(job=pk)
        job = Jobs.objects.get(id=pk)
        job.scheduled = False
        job.save()
        interview.delete()
        messages.success(request,f'Interview for {job.job_title} cancelled')
        return redirect('check_schedule')

    else:
        interview = Interviews.objects.get(job=pk) 
        return render(request, 'admin/cancel_interview.html',{'interview':interview})

#to view the leaves
@login_required
def admin_view_leaves(request,user=None):
    obj = EmployeeDesignation.objects.all() #for the department of employee
    if request.method == "POST":
        filter = request.POST['filter']
        if filter == 'month':
            if user:
                leaves = Leave.objects.filter(from_date__month = get_month(),user=user).order_by('-applied_date')
            else:
                leaves = Leave.objects.filter(from_date__month = get_month()).order_by('-applied_date')
        elif filter =='all':
            if user:
                leaves = Leave.objects.filter(user=user).order_by('-applied_date')
            else:
                leaves = Leave.objects.all().order_by('-applied_date')
        return render(request,'admin/admin_view_leaves.html',{'leaves':leaves,'obj':obj,'filter':filter})

    else:
        if user:
                leaves = Leave.objects.filter(user=user).order_by('-applied_date')
        else:
                leaves = Leave.objects.all().order_by('-applied_date')
        return render(request,'admin/admin_view_leaves.html',{'leaves':leaves,'obj':obj})

@login_required
def admin_leave_detail(request,pk):
    leave = Leave.objects.get(id = pk)
    #get current months leave counter
    month_counter = LeaveCounter.objects.get(date__month=get_month(),date__year=get_year(),user=leave.user) 
    year_counter = YearCounter.objects.get(date__year=get_year(),user=leave.user)
    context = {
        'leave':leave,
        'month_counter':month_counter,
        'year_counter':year_counter
    }
    return render(request,'admin/admin_leave_detail.html',context)

# to edit admin added leave    
@login_required
def admin_leave_edit(request,pk):
    attendance = Leave.objects.get(id = pk)  #leave is renamed to attendance
    #get current months leave counter
    leave_form = AdminLeaveForm(instance=attendance)
    month_counter = LeaveCounter.objects.get(date__month=get_month(),date__year=get_year(),user=attendance.user) 
    year_counter = YearCounter.objects.get(date__year=get_year(),user=attendance.user)
    context = {
        'form':leave_form,
        'attendance':attendance,
        'month':month_counter,
        'count':year_counter
    }
    if request.method == "POST":
        leave_form = AdminLeaveForm(request.POST,instance=attendance)
        if leave_form.is_valid():
            #leave balance check
            balance = get_balance(leave_form,attendance.user)
            leave_type = leave_form.cleaned_data['leave_type']
            if balance:
                messages.warning(request, f'Please check your {leave_type.upper()} availability')
                return render(request, 'admin/admin_leave_apply.html',context)
            leave_form.save()
            return redirect('admin_leave_detail',pk=pk)
    else:
        return render(request,'admin/admin_leave_apply.html',context)

@login_required
def approve_leave(request,pk):
    leave = Leave.objects.get(id=pk)
    if leave.approval != 'approved':
        leave_approval(leave)
        messages.success(request,f'Leave Approved')
        return redirect('admin_leave_detail',pk=pk)
        
    else:
        messages.info(request,f'Already Approved')
        return redirect('admin_leave_detail',pk=pk)

@login_required
def reject_leave(request,pk):
    leave = Leave.objects.get(id=pk)
    if leave.approval == 'approved':
        leave_reject(leave)
        messages.warning(request,f'Leave Rejected')
        return redirect('admin_leave_detail',pk=pk)
        
    else:
        if leave.approval == 'rejected':
            messages.info(request,f'Already Rejected')
        else:
            leave.approval = 'rejected'
            leave.save()
            messages.warning(request,f'Leave Rejected')

        return redirect('admin_leave_detail',pk=pk)

def leave_history(request):
    leaves = YearCounter.objects.filter(date__year=get_year())  
    obj = EmployeeDesignation.objects.all()
    context = {
        'leaves':leaves,
        'obj':obj
    }
    return render(request, 'admin/leave_history.html', context)

@login_required
def leave_history_detail(request,pk):
    year = YearCounter.objects.get(date__year=get_year(),user=pk)
    month = LeaveCounter.objects.filter(date__year=get_year(),user=pk) 
    employee = Newuser.objects.get(id=pk)   
    context = {
        'year':year,
        'month':month,
        'employee':employee
    }
    return render(request,'admin/leave_history_detail.html', context)

@login_required
def admin_attendance_view(request,user=None):
    if request.method == "POST":
      shift = request.POST['shift']
      if user:
            attendance =  Attendance.objects.filter(shift = shift,user=user).exclude(entry_time = None).order_by('-attendance_date')
      else:
            attendance =  Attendance.objects.filter(shift = shift).exclude(entry_time = None).order_by('-attendance_date')
      return render(request, 'admin/admin_attendance_view.html',{'attendance':attendance,'shift':shift})

    else:
        if user:
            attendance =  Attendance.objects.filter(shift='morning',user=user).exclude(entry_time = None).order_by('-attendance_date')
        else:
            attendance =  Attendance.objects.filter(shift='morning').exclude(entry_time = None).order_by('-attendance_date')

        return render(request, 'admin/admin_attendance_view.html',{'attendance':attendance})


@login_required
def admin_missing_regular(request):
    if request.method == "POST":
        filter = request.POST['filter']
        if filter == 'today':
            #todays attendance missing
            attendance =  Attendance.objects.filter(attendance_date =datetime.date.today(),shift='morning',entry_time=None).order_by('-attendance_date')
            for attendance in attendance:
                flag = leave_marked(attendance.user,attendance.attendance_date)
                if flag:
                    attendance.leave = True
                    attendance.save()
                else:          #if flag is false and leave is True (when rejected)
                    if attendance.leave == True:
                        attendance.leave = False
                        attendance.save()
                attendance =  Attendance.objects.filter(attendance_date =datetime.date.today(),shift='morning',entry_time=None).order_by('-attendance_date')
        
        elif filter == 'month':
            #this months attendance missing
            attendance =  Attendance.objects.filter(entry_time=None, attendance_date__month=get_month(),shift='morning').order_by('-attendance_date')
            for attendance in attendance:
                flag = leave_marked(attendance.user,attendance.attendance_date)
                if flag:
                    attendance.leave = True
                    attendance.save()
                else:          #if flag is false and leave is True (when rejected)
                    if attendance.leave == True:
                        attendance.leave = False
                        attendance.save()
            attendance =  Attendance.objects.filter(entry_time=None, attendance_date__month=get_month(),shift='morning').order_by('-attendance_date')


        elif filter == 'all':
            attendance =  Attendance.objects.filter(entry_time=None, shift='morning').order_by('-attendance_date')
            for attendance in attendance:
                flag = leave_marked(attendance.user,attendance.attendance_date)
                if flag:
                    attendance.leave = True
                    attendance.save()
                else:          #if flag is false and leave is True (when rejected)
                    if attendance.leave == True:
                        attendance.leave = False
                        attendance.save()
            attendance =  Attendance.objects.filter(entry_time=None, shift='morning').order_by('-attendance_date')
            
        return render(request, 'admin/admin_missing_regular.html',{'attendance':attendance,'filter':filter})

    else:
        attendance =  Attendance.objects.filter(entry_time=None, attendance_date = datetime.date.today(),shift='morning').order_by('-attendance_date')
        for attendance in attendance:
                flag = leave_marked( attendance.user,attendance.attendance_date)
                if flag:
                    attendance.leave = True
                    attendance.save()
                else:          #if flag is false and leave is True (when rejected)
                    if attendance.leave == True:
                        attendance.leave = False
                        attendance.save()
        attendance =  Attendance.objects.filter(entry_time=None, attendance_date = datetime.date.today(),shift='morning').order_by('-attendance_date')
        return render(request, 'admin/admin_missing_regular.html',{'attendance':attendance})



# to add leave by admin
@login_required
def admin_leave_apply(request,pk):
    attendance = Attendance.objects.get(id=pk)
    count = YearCounter.objects.get(user = attendance.user)
    month = LeaveCounter.objects.get(user = attendance.user, date__month=get_month())
    if request.method == "POST":
      leave_form = AdminLeaveForm(request.POST)
      if leave_form.is_valid():
         #leave balance check
         balance = get_balance(leave_form,attendance.user)
         leave_type = leave_form.cleaned_data['leave_type']
         if balance:
            messages.warning(request, f'Please check your {leave_type.upper()} availability')
            return render(request, 'admin/admin_leave_apply.html',{ 'form': leave_form,'attendance':attendance,'count':count,'month':month }) 

         leave = leave_form.save(False)
         leave.from_date = attendance.attendance_date
         leave.to_date = attendance.attendance_date
         leave.reason = "Leave Added by admin"
         leave.admin = True
         leave.user = attendance.user
         leave.save()
         return redirect('approve_leave', pk=leave.pk)  
      else:
         return render(request, 'admin/admin_leave_apply.html',{ 'form': leave_form, 'attendance':attendance,'count':count,'month':month })
    else:  
      form = AdminLeaveForm()
      return render(request, 'admin/admin_leave_apply.html',{ 'form': form, 'attendance':attendance,'count':count,'month':month })

#exit time not marked
@login_required
def exit_missing(request):
    if request.method == "POST":
        filter = request.POST['filter']
        if filter == 'today':
            #todays attendance missing
            attendance =  Attendance.objects.filter(attendance_date =datetime.date.today(),shift='morning',exit_time=None).exclude(entry_time = None).order_by('attendance_date')
        
        elif filter == 'month':
            #this months attendance missing
            attendance =  Attendance.objects.filter(exit_time=None, attendance_date__month=get_month(),shift='morning').exclude(entry_time = None).order_by('attendance_date')

        elif filter == 'all':
            attendance =  Attendance.objects.filter(exit_time=None, shift='morning').exclude(entry_time = None).order_by('attendance_date')
            
        return render(request, 'admin/exit_time_missing.html',{'attendance':attendance,'filter':filter})

    else:
        attendance =  Attendance.objects.filter(exit_time=None, attendance_date = datetime.date.today(),shift='morning').exclude(entry_time = None).order_by('attendance_date')
        return render(request, 'admin/exit_time_missing.html',{'attendance':attendance})

# Attendance Mark for Exit missing
@login_required
def exit_missing_mark(request,pk):
    attendance = Attendance.objects.get(id=pk)
    form = AdminAttendanceForm(instance=attendance)
    context = {
        'attendance':attendance,
        'form':form
    }
    if request.method == "POST":
        form = AdminAttendanceForm(request.POST ,instance=attendance)
        if form.is_valid():
            form.save()
            emp = attendance.user.first_name+' '+attendance.user.middle_name+' '+attendance.user.last_name
            messages.success(request,f'Exit time marked for {emp.upper()}')
            return redirect('admin_attendance_view')
    else:
        return render(request,'admin/admin_add_attendance.html',context)

#view night shift unmarked attendance:
@login_required
def night_unmarked(request):
    if request.method == "POST":
        filter = request.POST['filter']
        if filter == 'month':
            #this months attendance missing
            attendance =  Attendance.objects.filter(exit_time=None, attendance_date__month=get_month(),shift='night').exclude(entry_time = None).order_by('attendance_date')

        elif filter == 'all':
            attendance =  Attendance.objects.filter(exit_time=None, shift='night').exclude(entry_time = None).order_by('attendance_date')
            
        return render(request, 'admin/night_shift_unmarked.html',{'attendance':attendance,'filter':filter})

    else:
        attendance =  Attendance.objects.filter(exit_time=None, attendance_date__month=get_month(),shift='night').exclude(entry_time = None).order_by('attendance_date')
        return render(request, 'admin/night_shift_unmarked.html',{'attendance':attendance})


# Add an attendance to employee
@login_required
def add_emp_attendance(request,pk):
    emp = Newuser.objects.get(id=pk)
    form = AdminEmpAttendance()
    context = {
        'form':form,
        'emp':emp
    }
    if request.method == "POST":
        form = AdminEmpAttendance(request.POST)
        if form.is_valid():
            shift = form.cleaned_data['shift']
            date = form.cleaned_data['attendance_date']

            #to update the leve feild by checking if leave applied or not
            try:    
                attendance = Attendance.objects.get(attendance_date=date,user=pk,shift='morning')
                flag = leave_marked(pk,date)
                if flag:
                        attendance.leave = True
                        attendance.save()
                else:          #if flag is false and leave is True (when rejected)
                    if attendance.leave == True:
                        attendance.leave = False
                        attendance.save()
            except:
                messages.warning(request,f'Check your attendance date')
                return render(request,'admin/admin_emp_attendance.html',{'form':form,'emp':emp})



            if shift == 'morning':
                attendance = Attendance.objects.get(attendance_date=date, user=pk, shift='morning')
                if attendance:
                    if attendance.entry_time == None and attendance.exit_time == None and attendance.leave == False:
                        attendance.entry_time = form.cleaned_data['entry_time']
                        attendance.exit_time = form.cleaned_data['exit_time']
                        attendance.save()
                        messages.success(request,f'Attendance Marked')
                        return redirect('admin_attendance_view',user=pk)
                    else:
                        messages.warning(request,f'Failed to mark attendance')
                else:
                    messages.warning(request,f'Failed to mark attendance')
                return render(request,'admin/admin_emp_attendance.html',{'form':form,'emp':emp})
                
            #  night shift    
            else:
                if date > datetime.date.today():
                    messages.warning(request,f'Check your attendance date')
                    return render(request,'admin/admin_emp_attendance.html',{'form':form,'emp':emp})
                else:
                    leave = form.save(False)
                    leave.user = emp
                    leave.save()
                    messages.success(request,f'Attendance Added')
                    return redirect('admin_attendance_view',user=pk)
    else:
        return render(request,'admin/admin_emp_attendance.html',context)

# Attendance regularization 
@login_required
def admin_regularize(request):
    attendance = AttendanceRegularization.objects.all().order_by('-id')
    context = {
        'attendance':attendance
    }
    return render(request,'admin/admin_regularization.html',context)

#apply regualrization
def apply_regularization(request,pk):
    attendance = AttendanceRegularization.objects.get(id=pk)
    id = attendance.attendance_id
    print(id)
    form = AdminRegularizationForm(instance=attendance)
    context = {
        'attendance':attendance,
        'form':form
    }
    if request.method == "POST":
        form = AdminRegularizationForm(request.POST, instance=attendance)
        if form.is_valid():
            old_attendance = Attendance.objects.get(id=id) 
            old_attendance.entry_time = form.cleaned_data['new_entry']
            old_attendance.exit_time = form.cleaned_data['new_exit']
            old_attendance.save()
            attendance.status = 'approved'
            attendance.save()
            messages.success(request, f'Regularization Approved')
            return redirect('admin_regularize')

    return render(request,'admin/admin_regularization_detail.html', context)

#reject regularization
@login_required
def reject_regularization(request,pk):
    attendance = AttendanceRegularization.objects.get(id=pk)
    id = attendance.attendance_id
    if attendance.status == 'approved':
        old_attendance = Attendance.objects.get(id=id)
        old_attendance.entry_time = attendance.old_entry
        old_attendance.exit_time = attendance.old_exit
        old_attendance.save()
        attendance.status = 'rejected'
    else:
        attendance.status = 'rejected'
    attendance.save()
    messages.warning(request, f'Regularization rejected')
    return redirect('admin_regularize')


#notification 
@login_required
def add_notification(request):
    form = MessageForm()
    message = Messages.objects.all().order_by('-id')
    count = Messages.objects.all().count()
    context = {
        'message':message,
        'count':count,
        'form':form
    }
    if request.method == "POST":
        if "search" in request.POST:
            value = request.POST['search_msg']
            message = Messages.objects.filter(Q (title__icontains=value) | Q(date__icontains=value)).order_by('-id')
            c = message.count()
            if c == 0:
                messages.info(request,f'No results found')
                return redirect('add_notification')
            else:
                p = Paginator(message,5)  # second argument is no of items to be displayed
                page_num = request.GET.get('page',1 ) #get the page no by url  and 1 is default
                try:
                    page = p.page(page_num)
                except EmptyPage:
                    page = p.page(1)
                return render(request, 'admin/add_notifications.html',{'message':page,'count':count,'form':form})
        
        elif "add" in request.POST:
            form = MessageForm(request.POST)
            if form.is_valid():
                msg = form.save(False)
                msg.date = datetime.datetime.now()
                msg.save()
                messages.success(request,'Message Added')
                return redirect('add_notification')
    
    else:
        if count != 0:
            p = Paginator(message,5)  # second argument is no of items to be displayed
            page_num = request.GET.get('page',1 ) #get the page no by url  and 1 is default
            try:
               page = p.page(page_num)
            except EmptyPage:
               page = p.page(1)
            return render(request, 'admin/add_notifications.html',{'message':page,'count':count,'form':form})
        else:
            return render(request, 'admin/add_notifications.html',context)

# edit notification
@login_required
def edit_notification(request,pk):
    message = Messages.objects.get(id=pk)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message Edited')
            return redirect('add_notification')
    else:
        form = MessageForm(instance=message)
        return render(request, 'admin/edit_notification.html',{'form':form})

#view message
@login_required
def view_notification(request,pk):
    message = Messages.objects.get(id=pk)
    return render(request, 'admin/view_message.html',{'message':message})

#delete message
@login_required
def delete_notification(request,pk):
    message = Messages.objects.get(id=pk)
    if request.method == "POST":
        message.delete()
        messages.warning(request,f'Message Deleted')
        return redirect('add_notification')
    else:
        return render(request, 'admin/delete_message.html',{'message':message})


#payroll month select
@login_required
def payroll_month(request):
    if request.method == "POST":
        date = request.POST['date']
        datem = datetime.datetime.strptime(date, "%Y-%m-%d")
        today = datetime.date.today()
        if  datem.year == today.year:
                if datem.month < today.month:
                    payroll = Payroll.objects.filter(date__month__gte=datem.month, date__year__gte=datem.year).count()
                    if payroll == 0:
                        return redirect('calculate_payroll',cdate=datem)

                    else:
                        messages.info(request,f'Payroll Already Calculated')
                        return redirect('payroll_month')
                else:
                    messages.warning(request,f'Select a valid month and year')
                    return redirect('payroll_month')
               
        elif  datem.year < today.year:
                payroll = Payroll.objects.filter(date__month__gte=datem.month, date__year__gte=datem.year).count()
                if payroll == 0:
                    return redirect('calculate_payroll',cdate=datem)
                else:
                    messages.info(request,f'Payroll Already Calculated')
                    return redirect('payroll_month')

        else:
                    messages.warning(request,f'Select a valid month and year')
                    return redirect('payroll_month')

    else:
         return render(request,'admin/payroll_month_selector.html')


#calculate payroll
@login_required
def calculate_payroll(request,cdate):
    cdate = datetime.datetime.strptime(cdate, "%Y-%m-%d %H:%M:%S")
    calculate_salary(cdate)
    messages.success(request, f'Calculation completed')
    return redirect('view_payroll', vdate = cdate)
    
#payroll view month select
@login_required
def view_payroll_month(request):
    if request.method == "POST":
        date = request.POST['date']
        datem = datetime.datetime.strptime(date, "%Y-%m-%d")
        payroll = Payroll.objects.filter(date__month=datem.month, date__year=datem.year).count()
        if payroll != 0:
            return redirect('view_payroll', vdate=datem)
        else:
            messages.warning(request,f'Not Available, please check your date')
            return redirect('view_payroll_month')
    else:
        return render(request, 'admin/payroll_view_month.html')

#view payroll
@login_required
def view_payroll(request,vdate):
    try:
        vdate = datetime.datetime.strptime(vdate, "%Y-%m-%d %H:%M:%S")
    except:
        vdate = datetime.datetime.strptime(vdate, "%Y-%m-%d")

    payroll = Payroll.objects.filter(date__month=vdate.month, date__year=vdate.year)
    obj = EmployeeDesignation.objects.all()
    context = {
        'payroll':payroll,
        'obj':obj,
        'vdate':vdate
    }
    return render(request, 'admin/view_payroll.html',context)

#hold salary
@login_required
def hold_salary(request, pk):
    salary = Payroll.objects.get(id=pk)
    emp = salary.user.first_name+' '+salary.user.middle_name+' '+salary.user.last_name
    if salary.status == 'hold':
        salary.status = 'pending'
        messages.success(request,f'Salary unholded for {emp.upper()}')
    else:
        salary.status = 'hold'
        messages.warning(request,f'Salary holded for {emp.upper()}')
    vdate = salary.date
    salary.save()
    return redirect('view_payroll', vdate = vdate)

#approve salary
@login_required
def approve_salary(request,pk):
    salary = Payroll.objects.get(id=pk)
    emp = salary.user.first_name+' '+salary.user.middle_name+' '+salary.user.last_name
    salary.status = 'approved'
    salary.save()
    vdate = salary.date
    messages.success(request,f'Salary Approved for {emp.upper()}')
    return redirect('view_payroll', vdate = vdate)


#view salary slip
@login_required
def salary_slip(request, pk):
    payroll = Payroll.objects.get(id=pk)
    emp = Newuser.objects.get(id = payroll.user.id)
    designation = EmployeeDesignation.objects.get(user = payroll.user.id)
    context = {
        'payroll':payroll,
        'emp':emp,
        'designation':designation
    }
    return render(request, 'admin/salary_slip.html',context)

#edit payroll
@login_required
def edit_payroll(request,pk):
    payroll = Payroll.objects.get(id=pk)
    form = PayrollEditForm()
    vdate = payroll.date
    if request.method == "POST":
        form = PayrollEditForm(request.POST)
        if form.is_valid():
            payroll.net_salary = payroll.net_salary + float(form.cleaned_data['other_benefits'])
            
            payroll.net_salary = payroll.net_salary - float(form.cleaned_data['other_deductions'])

            payroll.other_benefits = payroll.other_benefits + float(form.cleaned_data['other_benefits'])
            payroll.other_deductions = payroll.other_deductions +  float(form.cleaned_data['other_deductions'])

            payroll.save()
            messages.success(request, f'Payroll Edited Successfully')
            return redirect('view_payroll', vdate = vdate)
    else:
        return render(request, 'admin/edit_payroll.html',{'payroll':payroll,'form':form})

# to approve all pending payrolls 
@login_required
def approve_all_payroll(request, vdate):
    vdate = datetime.datetime.strptime(vdate, "%Y-%m-%d %H:%M:%S")
    payrolls = Payroll.objects.filter(status='pending',date=vdate)
    for payroll in payrolls:
        payroll.status = 'approved'
        payroll.save()
    messages.success(request, f'Payrolls Approved')
    return redirect('view_payroll', vdate = vdate)

#add holidays
@login_required
def holidays(request):
    holidays = Holidays.objects.all().order_by('-date')
    form = HolidayForm()
    if request.method == "POST":
        form = HolidayForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            attendance = Attendance.objects.filter(attendance_date = date)
            if attendance:
                for attendance in attendance:
                    attendance.holiday = True
                    attendance.save()
            form.save()
            messages.success(request,f'Holiday Added')
            return redirect('holidays')
    else:
        return render(request,'admin/admin_holidays.html',{'holidays':holidays,'form':form})
    
#edit holidays
@login_required
def holiday_edit(request,pk):
    holiday = Holidays.objects.get(id = pk)
    form = HolidayForm(instance=holiday)
    if request.method == "POST":
        att = Attendance.objects.filter(attendance_date = holiday.date)
        if att:
            for att in att:
                att.holiday = False
                att.save()
        form = HolidayForm(request.POST,instance=holiday)
        if form.is_valid():
            date = form.cleaned_data['date']
            attendance = Attendance.objects.filter(attendance_date = date)
            if attendance:
                for attendance in attendance:
                    attendance.holiday = True
                    attendance.save()
            form.save()
            messages.success(request,f'Holiday Edited')
            return redirect('holidays')
    else:
        return render(request, 'admin/holiday_edit.html',{'form':form})

#delete holiday
@login_required
def delete_holiday(request,pk):
    holiday = Holidays.objects.get(id = pk)
    if request.method == "POST":
        att = Attendance.objects.filter(attendance_date = holiday.date)
        if att:
            for att in att:
                att.holiday = False
                att.save()
        holiday.delete()
        messages.success(request,f'Holiday Deleted')
        return redirect('holidays')
    else:
        return render(request,'admin/delete_holiday.html',{'holiday':holiday})