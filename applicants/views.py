from queue import Empty
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage
from base.models import Jobs

# list view of jobs 

def jobs(request):
    jobs = Jobs.objects.order_by('-posted_on')
    
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