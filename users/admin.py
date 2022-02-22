from django.contrib import admin
from .models import Newuser,ApplicantProfile
from django.contrib.auth.admin import UserAdmin






class UserAdminConfig(UserAdmin):
    
    #displaying the table
    search_fields=('email','first_name','middle_name','last_name')
    list_filter=('email','first_name')
    ordering=['-date_joined']
    list_display = ('email', 'first_name','middle_name','last_name','is_employee', 'is_applicant' )


    #this defines the fields when we click on an added user(ordering)
    fieldsets = [
    [None,{'fields': ['email','first_name','middle_name','last_name']}],
    ['permissions',{'fields': ['is_employee','is_applicant','is_staff','is_active']}],
    ]


    add_fieldsets=[
        [None,{'classes':('wide'),
                'fields':['first_name','middle_name','last_name','email','password1','password2','is_employee','is_applicant','is_staff','is_active']}
        ],
    ]


admin.site.register(Newuser, UserAdminConfig)
admin.site.register(ApplicantProfile)


