from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_home, name='admin_home'),
    path('add_employee',views.add_employee, name='add_employee'),
    path('view_employee',views.view_employee, name='view_employee'),
]