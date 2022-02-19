from django.shortcuts import render
from .models import Jobs

def index(request):
     
     jobs = Jobs.objects.order_by('-posted_on')[:3]

     return render(request, 'base/index.html',{'jobs':jobs})

