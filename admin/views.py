from dataclasses import field
import logging
from statistics import mode
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from admin.forms import AddEmployeeForm, DesignationForm, EditEmployeeForm, SalaryForm
from django.contrib import messages
from admin.models import Designations, Salary
from base.models import Department
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
