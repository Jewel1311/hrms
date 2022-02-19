from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.jobs, name='jobs'),
    path('job-detail/<str:job_id>/', views.job_detail, name='job-detail'),
   
]