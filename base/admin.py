from tabnanny import verbose
from django.contrib import admin
from .models import Department, Jobs   


class JobsAdmin(admin.ModelAdmin):
    ordering = ['-posted_on']
    search_fields = ('job_title','location','department','posted_on','withdraw_date')
    list_filter = ('job_title','location','department')
    list_display = ('job_title','location','department','posted_on','withdraw_date' )

admin.site.register(Department)
admin.site.register(Jobs,JobsAdmin)

