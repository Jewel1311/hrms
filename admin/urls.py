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
    path('applications/<int:pk>/',views.applications, name='applications'),
    path('applicant_status/<int:id>/<int:jobid>/<str:btn>/',views.applicant_status, name='applicant_status'),
]