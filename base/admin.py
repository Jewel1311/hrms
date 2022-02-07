from tabnanny import verbose
from django.contrib import admin
from .models import Category, Jobs   


class JobsAdmin(admin.ModelAdmin):
    ordering = ['-posted_on']
    search_fields = ('job_title','location','category','posted_on','withdraw_date')
    list_filter = ('job_title','location','category')
    list_display = ('job_title','location','category','posted_on','withdraw_date' )

admin.site.register(Category)
admin.site.register(Jobs, JobsAdmin)

