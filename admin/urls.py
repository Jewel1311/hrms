from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_home, name='admin_home'),
    path('add_employee/',views.add_employee, name='add_employee'),
    path('view_employee/',views.view_employee, name='view_employee'),
    path('employee_detail/<int:pk>/',views.employee_detail, name='employee_detail'),
    path('employee_edit/<int:pk>/',views.employee_edit, name='employee_edit'),
    path('delete_employee/<int:pk>/',views.delete_employee, name='delete_employee'),
    path('department/',views.department, name='department'),
    path('designations/',views.designations, name='designations'),
    path('designation_edit/<int:pk>/',views.designation_edit, name='designation_edit'),
    path('department_edit/<int:pk>/',views.department_edit, name='department_edit'),
    path('delete_department/<int:pk>/',views.DeleteDepartment.as_view(), name='delete_department'),
    path('delete_designation/<int:pk>/',views.DeleteDesignation.as_view(), name='delete_designation'),
    path('add_jobs/',views.add_jobs, name='add_jobs'),
    path('view_jobs/',views.view_all_jobs, name='view_all_jobs'),
    path('job_detail_view/<slug:slug>/',views.job_detail_view, name='job_detail_view'),
    path('edit_job/<int:pk>/',views.EditJob.as_view(), name='edit_job'),
    path('delete_job/<int:pk>/',views.delete_job, name='delete_job'),
    path('view_applicants/',views.view_applicants, name='view_applicants'),
    path('applicant_details/<int:pk>/',views.applicant_details, name='applicant_details'),
    path('delete_applicants/<int:pk>/',views.delete_applicants, name='delete_applicants'),
    path('applications/<int:pk>/',views.applications, name='applications'),
    path('applicant_status/<int:id>/<int:jobid>/<str:btn>/',views.applicant_status, name='applicant_status'),
    path('add_interviews/<int:pk>/',views.add_interview, name='add_interview'),
    path('check_schedule/',views.check_schedule, name='check_schedule'),
    path('scheduled_interviews/<int:pk>/',views.scheduled_interviews, name='scheduled_interviews'),
    path('edit_interviews/<int:pk>/',views.edit_interviews, name='edit_interviews'),
    path('selected_applicants/<int:pk>/',views.selected_applicants, name='selected_applicants'),
    path('cancel_interview/<int:pk>/',views.cancel_interview, name='cancel_interview'),
    path('admin_view_leaves/',views.admin_view_leaves, name='admin_view_leaves'),
    path('admin_view_leaves/<int:user>/',views.admin_view_leaves, name='admin_view_leaves'),
    path('admin_leave_detail/<int:pk>/',views.admin_leave_detail, name='admin_leave_detail'),
    path('approve_leave/<int:pk>/',views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:pk>/',views.reject_leave, name='reject_leave'),
    path('leave_history/',views.leave_history, name='leave_history'),
    path('leave_history_detail/<int:pk>/',views.leave_history_detail, name='leave_history_detail'),
    path('admin_attendance_view/', views.admin_attendance_view , name='admin_attendance_view'),
    path('admin_attendance_view/<int:user>/', views.admin_attendance_view , name='admin_attendance_view'),
    path('admin_missing_regular/', views.admin_missing_regular , name='admin_missing_regular'),
    path('exit_time_missing/', views.exit_missing , name='exit_time_missing'),
    path('admin_leave_apply/<int:pk>/', views.admin_leave_apply , name='admin_leave_apply'),
    path('admin_leave_edit/<int:pk>/', views.admin_leave_edit , name='admin_leave_edit'),
    path('exit_missing_mark/<int:pk>/', views.exit_missing_mark , name='exit_missing_mark'),
    path('night_unmarked/', views.night_unmarked , name='night_unmarked'),
    path('add_employee_attendance/<int:pk>/', views.add_emp_attendance , name='add_emp_attendance'),

]
