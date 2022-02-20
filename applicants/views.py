import datetime
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
from applicants.models import Applications
from base.models import Jobs

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
    context = { 'job_id':job_id}
    return render(request,'applicant/jobdetail.html',context)


@login_required
def apply_now(request,job_id):
   application = Applications()
   application.user = request.user
   application.job = job_id
   return render(request, 'applicant/applicant-home')