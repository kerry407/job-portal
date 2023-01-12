from django.urls import path 
from . import views 

urlpatterns = [
    path("post-job/", views.CreateJobPostView.as_view(), name="post-job"),
    path("job-list/", views.JobPostListView.as_view(), name="job-list"),
    path("job-post-detail/<slug:slug>/", views.JobPostDetailView.as_view(), name="job-post-detail"),
    path("apply-job/<slug:slug>/", views.ApplyJobView.as_view(), name='apply-job'),
    path("job-application-detail/<uuid:pk>/", views.JobApplicationDetailView.as_view(), name="job-application-detail"),
    path("job-application-list/", views.JobApplicationListView.as_view(), name="job-application-list")
]
