from queue import Empty
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage
from base.models import Jobs

def jobs(request):
    jobs = Jobs.objects.all()
    
    p = Paginator(jobs,1)  # second argument is no of items to be displayed
   
    page_num = request.GET.get('page',1 ) #get the page no by url  and 1 is default
    try:
       page = p.page(page_num)
    except EmptyPage:
       page = p.page(1)

    return render(request, 'applicant/jobview.html',{'jobs': page})