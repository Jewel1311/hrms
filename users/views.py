from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ApplicantProfile, Newuser, Newuser
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

        uid=request.user.id                               #get the primary key of currently login user

        # to take the profile associated with user using the primary key and  phone number not set  
        
        profile=ApplicantProfile.objects.filter(user=uid).filter(phone='').count()

        if profile:
           return render(request, 'applicant/fillprofile.html') #go to fill details page

        else:
           return render(request, 'applicant/applicant-home.html')  #go to user home page

    elif request.user.is_employee:
        return render(request, 'users/employee.html')
 

