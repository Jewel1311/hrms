from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_home,name='employee-home'),
    path('profile/',views.employee_profile,name='employee_profile'),
    path('profile-view/',views.view_employee_profile ,name='view_employee_profile'),
    path('morning_shift/', views.morning_shift , name='morning_shift'),
    path('night_shift/', views.night_shift , name='night_shift'),
    path('attendance_view/', views.attendance_view , name='attendance_view'),
    path('apply_leave/', views.apply_leave , name='apply_leave'),
    path('view_leave/', views.view_leave , name='view_leave'),
]