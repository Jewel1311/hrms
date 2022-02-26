from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.jobs, name='jobs'),
    path('job-detail/<str:job_id>/', views.job_detail, name='job-detail'),
    path('apply_confirmation/<str:job_id>/', views.apply_confirmation, name='apply_confirmation'),
    path('apply_now/<str:job_id>/', views.apply_now, name='apply_now'),
    path('save_applicant_profile/', views.save_applicant_profile, name='save_applicant_profile'),
    path('view_applicant_profile/', views.view_applicant_profile, name='view_applicant_profile'),
    path('applied/', views.applied, name='applied'),
    path('interviews/', views.interviews, name='interviews'),
   
] 