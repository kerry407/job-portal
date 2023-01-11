from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ["id", "job_title", "company", "date_posted"]
    list_filter = ["company", "date_posted"]
    
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "job_post", "applicant"]
    list_filter = ["job_post", "applicant"]