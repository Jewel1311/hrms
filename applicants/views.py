import datetime 
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
from applicants.models import Applications
from base.models import Jobs
from users.models import ApplicantProfile

# list view of jobs 

def jobs(request):
   today = datetime.date.today()
   jobs = Jobs.objects.filter(withdraw_date__gte=today).order_by('-posted_on')
   if request.method == "POST":
        value = request.POST['search_jobs']
        print(value)
        jobs = Jobs.objects.filter(Q (job_title__icontains=value) | Q(location__icontains = value)).filter(withdraw_date__gte=today).order_by('-posted_on')
   count = jobs.count()
   
   if count == 0:
       messages.success(request, f'No results found')
       return render(request, 'applicant/jobview.html')

   else:
      
       p = Paginator(jobs,5)  # second argument is no of items to be displayed
       page_num = request.GET.get('page',1 ) #get the page no by url  and 1 is default
       try:
          page = p.page(page_num)
       except EmptyPage:
          page = p.page(1)
       return render(request, 'applicant/jobview.html',{'jobs': page})
   

# detailed view of jobs

def job_detail(request, job_id):
    job_id = Jobs.objects.get(id=job_id)
    context = { 'job_id':job_id }
    return render(request,'applicant/jobdetail.html',context)



@login_required
def apply_confirmation(request,job_id):
   job = Jobs.objects.get(id=job_id) 
   return render(request, "applicant/apply_confirmation.html",{'job':job })

@login_required
def apply_now(request,job_id):
   application = Applications()
   job = Jobs.objects.get(pk=job_id)  #select the Jobs instance using job id 
   profile = ApplicantProfile.objects.get(user=request.user) #select the appliant profile for setting last applied


  # this checks last job apply of the user
   if profile.last_apply is not None:
      diff = datetime.date.today() - profile.last_apply 
      diff = diff.days                                   #convert the date field to days
   else:
      diff = 90

   if diff >= 90:
      application.user = request.user
      application.job = job   #save the foreign key using the selected instance
      application.save()
      profile.last_apply = datetime.date.today()  #changes the last apply date to current date in applicant profile
      profile.save()
      return render(request, 'applicant/applicant-home.html')
   else:
       messages.success(request, f'No results found')
       return render(request, 'applicant/jobview.html')

@login_required
def save_applicant_profile(request):
   if request.method == "POST":
      addressline1 = request.POST['addressline1']
      place = request.POST['place']
      city = request.POST['city']
      state = request.POST['state']
      mobile = request.POST['mobile']
      pin = request.POST['pin']
      dob = request.POST['dob']
      cv = request.POST['cv']

      if len(mobile)!=10:
         messages.warning(request, f'Phone number must be 10 digits')
         return render(request, 'applicant/fillprofile.html')
      elif len(pin) != 6:
         messages.warning(request, f'Postcode must be 6 digits')
         return render(request, 'applicant/fillprofile.html')

      else:
         return render(request, 'applicant/fillprofile.html')