from django.urls import reverse_lazy
from django.views.generic import DeleteView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from admin.forms import AddEmployeeForm, DesignationForm, EditEmployeeForm, JobForm, SalaryForm
from django.contrib import messages
from admin.models import Designations, Salary
from base.models import Department, Jobs
from employees.models import EmployeeDesignation
from users.models import Newuser


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
    employees = Newuser.objects.filter(is_employee = True)
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
def view_all_jobs(request):
    jobs = Jobs.objects.all()
    return render(request, 'admin/view_jobs.html',{ 'jobs':jobs })

#detailed job view
def job_detail_view(request,slug):
    job_id = Jobs.objects.get(id = slug)
    return render(request, 'admin/admin_jobdetail_view.html',{'job_id': job_id})

#edit Job
class EditJob(SuccessMessageMixin,UpdateView):
   model = Jobs
   form_class = JobForm
   template_name = 'admin/add_jobs.html'
   success_message = "Job Updated"

@login_required
def delete_job(requset,pk):
    job = Jobs.objects.get(id=pk)
    job.delete()
    messages.success(requset,f'Job Deleted')
    return redirect('view_all_jobs')

def view_applicants(request):
    applicants = Newuser.objects.filter(is_applicant=True)
    return render(request,'admin/view_applicants.html',{ 'applicants':applicants})