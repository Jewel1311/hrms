from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.jobs, name='jobs'),
   
]