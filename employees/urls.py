from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_home,name='employee-home'),
    path('profile/',views.employee_profile,name='employee_profile'),
    path('profile-view/',views.view_employee_profile ,name='view_employee_profile')
]