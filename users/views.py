from django.shortcuts import render,redirect
from .models import ApplicantProfile, Newuser, Newuser
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views.generic import CreateView

def registerion(request):
    if request.method == "POST":
        
        reg_form = UserRegistrationForm(request.POST)

        applicant=ApplicantProfile()                                             #instance of model Applicant profile

        if reg_form.is_valid():

                                                                                #setting the some values of applicant table
            applicant.first_name = reg_form.cleaned_data['first_name']
            applicant.middle_name = reg_form.cleaned_data['middle_name']
            applicant.last_name = reg_form.cleaned_data['last_name']

            user = reg_form.save(False)

            user.is_applicant = True                                             # to set the registerd user is an applicant
            user.save()

            applicant.user = user                                                #connecting both tables

            applicant.save()

            messages.success(request, f'Registered Successfully')
            return redirect('register')


    else:
        reg_form=UserRegistrationForm()

    return render(request, "users/register.html", {'reg_form': reg_form})

class RegisterView(CreateView):
    model = Newuser
    form_class = UserRegistrationForm
    template_name = 'users/register.html' 
