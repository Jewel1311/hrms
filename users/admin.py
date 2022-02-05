from django.contrib import admin
from .models import Login,ApplicantProfile
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):

    #displaying the table
    search_fields=('email','first_name','middle_name','last_name')
    list_filter=('email','first_name')
    ordering=['-date_joined']
    list_display = ('email', 'first_name','middle_name','last_name', 'is_applicant', 'is_employee','is_project_manager')


    #this defines the fields when we click on an added user(ordering)
    fieldsets = [
    [None,{'fields': ['email','first_name','middle_name','last_name']}],
    ['permissions',{'fields': ['is_applicant','is_employee','is_staff','is_active']}],
    ]


    add_fieldsets=[
        [None,{'classes':('wide'),
                'fields':['first_name','middle_name','last_name','email','password1','password2','is_employee','is_applicant','is_project_manager','is_staff','is_active']}
        ],
    ]

class Applicantadmin(admin.ModelAdmin):
    list_display=('first_name','last_name')



 

admin.site.register(Login, UserAdminConfig)
admin.site.register(ApplicantProfile,Applicantadmin)


