from django.shortcuts import render
from base.models import Jobs

def jobs(request):
    jobs=Jobs.objects.all()
    return render(request, 'applicant/jobview.html',{'jobs': jobs})