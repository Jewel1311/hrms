from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_home,name='employee-home'),
    path('change_pasword/',views.MyPasswordChangeView.as_view(), name='employee-password-change'),
    path('profile/',views.employee_profile,name='employee_profile'),
    path('profile-view/',views.view_employee_profile ,name='view_employee_profile'),
    path('morning_shift/', views.morning_shift , name='morning_shift'),
    path('night_shift/', views.night_shift , name='night_shift'),
    path('attendance_view/', views.attendance_view , name='attendance_view'),
    path('apply_leave/', views.apply_leave , name='apply_leave'),
    path('view_leave/', views.view_leave , name='view_leave'),
    path('leave_detail/<slug:slug>/',views.leave_detail, name='leave_detail'),
    path('leave_edit/<int:pk>/',views.EditLeave.as_view(), name='leave_edit'),
    path('regularization/',views.selected_attendance, name='selected_attendance'),
    path('attendace_regularization/<str:pk>/',views.attendance_regularization, name='attendance_regularization'),
    path('attendace_regularization/',views.regularization_requests, name='regularization_requests'),
    path('view_notification/',views.view_notification, name='view_notification'),
    path('notification_detail/<int:pk>/',views.notification_detail, name='notification_detail'),
    path('emp_payroll_month/',views.emp_payroll_month, name='emp_payroll_month'),
    path('emp_salary_slip/<str:vdate>/', views.emp_salary_slip, name='emp_salary_slip'),
]