from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_home, name='admin_home'),
    path('add_employee/',views.add_employee, name='add_employee'),
    path('view_employee/',views.view_employee, name='view_employee'),
    path('employee_detail/<int:pk>/',views.employee_detail, name='employee_detail'),
    path('employee_edit/<int:pk>/',views.employee_edit, name='employee_edit'),
    path('delete_employee/<int:pk>/',views.delete_employee, name='delete_employee'),
]