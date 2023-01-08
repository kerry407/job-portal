from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ["job_title", "company", "date_posted"]
    list_filter = ["company", "date_posted"]