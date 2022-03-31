import datetime
from .tasks import counter, get_month,get_year,set_leave
from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView,ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from admin.forms import AddEmployeeForm, DesignationForm, EditEmployeeForm, InterviewForm, JobForm, SalaryForm
from django.contrib import messages
from admin.models import Designations, Salary
from applicants.models import Applications, Interviews
from base.models import Department, Jobs
from base.views import leave_counter
from employees.models import EmployeeDesignation, Leave, LeaveCounter
from users.models import ApplicantProfile, Newuser


@login_required
def admin_home(request):
    return render(request, 'admin/admin-home.html')


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

            LeaveCounter.objects.create(cl=0,el=0,lp=0,sl=0,user=user)
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
        print(id)
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
def admin_view_leaves(request):
    leaves = Leave.objects.all().order_by('-id')
    obj = EmployeeDesignation.objects.all() #for the department of employee
    return render(request,'admin/admin_view_leaves.html',{'leaves':leaves,'obj':obj})

@login_required
def admin_leave_detail(request,pk):
    leave = Leave.objects.get(id = pk)
    #get current months leave counter
    month_counter = LeaveCounter.objects.get(date__month=get_month(),date__year=get_year(),user=leave.user) 
    year_counter = counter(leave) # call function in tasks.py
    context = {
        'leave':leave,
        'month_counter':month_counter,
        'year_counter':year_counter
    }
    return render(request,'admin/admin_leave_detail.html',context)

@login_required
def approve_leave(request,pk):
    leave = Leave.objects.get(id=pk)
    if leave.approval != 'approved':
        number = set_leave(leave)  #return the  number of days
        count = LeaveCounter.objects.get(date__month=get_month(),date__year=get_year(),user=leave.user)
        if leave.leave_type == 'casual leave':
            count.cl = count.cl + number
        elif leave.leave_type == 'earned leave':
            count.el = count.el + number
        elif leave.leave_type == 'loss of pay':
            count.lp = count.lp + number
        elif leave.leave_type == 'sick leave':
            count.sl = count.sl + number
        count.save()
        leave.approval = 'approved'
        leave.save()
        messages.success(request,f'Leave Approved')
        return redirect('admin_leave_detail',pk=pk)
        
    else:
        messages.info(request,f'Already Approved')
        return redirect('admin_leave_detail',pk=pk)

@login_required
def reject_leave(request,pk):
    leave = Leave.objects.get(id=pk)
    if leave.approval == 'approved':
        number = set_leave(leave)  #return the  number of days
        count = LeaveCounter.objects.get(date__month=get_month(),date__year=get_year(),user=leave.user)
        if leave.leave_type == 'casual leave':
            count.cl = count.cl - number
        elif leave.leave_type == 'earned leave':
            count.el = count.el - number
        elif leave.leave_type == 'loss of pay':
            count.lp = count.lp - number
        elif leave.leave_type == 'sick leave':
            count.sl = count.sl - number
        count.save()
        leave.approval = 'rejected'
        leave.save()
        messages.warning(request,f'Leave Rejected')
        return redirect('admin_leave_detail',pk=pk)
        
    else:
        if leave.approval == 'rejected':
            messages.info(request,f'Already Rejected')
        else:
            leave.approval = 'rejected'
            messages.warning(request,f'Leave Rejected')

        return redirect('admin_leave_detail',pk=pk)

def leave_history(request):
    leaves = LeaveCounter.objects.filter(date__year=get_year())
    obj = EmployeeDesignation.objects.all()
    context = {
        'leaves':leaves,
        'obj':obj
    }
    return render(request, 'admin/leave_history.html', context)

# @login_required
# def leave_history_detail(request):