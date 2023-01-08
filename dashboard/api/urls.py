from django.urls import path 
from . import views 

urlpatterns = [
    path("post-job/", views.CreateJobPostView.as_view(), name="post-job")
]
