from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from employees.models import EmployeeProfile
from .models import ApplicantProfile
from .forms import UserRegistrationForm
from django.contrib import messages



def register(request):
    if request.method == "POST":

        reg_form = UserRegistrationForm(request.POST)
                                             
       
        if reg_form.is_valid():

            user=reg_form.save(False)
            user.is_applicant=True
            user.save()
          


            messages.success(request, f'Registered Successfully')
            return redirect('login')


    else:
        reg_form=UserRegistrationForm()

    return render(request, "users/register.html", {'reg_form': reg_form})


@login_required
def filterlogin(request):

    if request.user.is_applicant:  #checking if the login user is an applicant
        profile = ApplicantProfile.objects.filter(user=request.user)
        if profile:
           return redirect('jobs')
        else:
           return redirect('save_applicant_profile')
       

    elif request.user.is_employee:
        profile = EmployeeProfile.objects.filter(user = request.user).count()
        if profile:
           return redirect('employee-home')
        else:
            return redirect('employee_profile')
 

