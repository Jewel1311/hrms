import datetime
from django.shortcuts import render
from .models import Jobs

def index(request):
     
     jobs = Jobs.objects.filter(withdraw_date__gte=datetime.date.today()).order_by('-posted_on')[:3]

     return render(request, 'base/index.html',{'jobs':jobs})

