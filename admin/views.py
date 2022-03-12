from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin.forms import AddEmployeeForm, DesignationForm, SalaryForm
from django.contrib import messages

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

# view the employees 
@login_required
def view_employee(request):
    employees = Newuser.objects.filter(is_employee = True)
    return render(request, 'admin/employee-view.html',{'employees':employees})
