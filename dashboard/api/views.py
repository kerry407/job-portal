from datetime import datetime 
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from ..models import JobPost, JobApplication
from .serializers import JobPostSerializer, JobApplicationSerializer, JobApplicationSerializerForPoster
from .pagination import CustomPagination
from .permissions import IsEmployer, JobPosterOrReadOnly, JobApplicantOnly
from .renderers import CustomRenderer


class CreateJobPostView(CreateAPIView):
    permission_classes = [IsEmployer]
    serializer_class = JobPostSerializer
    
    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(poster=user)


class JobPostListView(ListAPIView):
    serializer_class = JobPostSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["contract_type", "location", "working_language", "job_category", "industry"]
    search_fields = ["company", "job_title", "job_category", "industry"]
    ordering_fields = ["date_posted", "last_updated"]
    pagination_class = CustomPagination 
    renderer_classes = [CustomRenderer]
    
    def get_queryset(self):
        return JobPost.objects.filter(deadline__gte=datetime.today().date().strftime('%Y-%m-%d')).order_by("-last_updated")
    
    
    
        
class JobPostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [JobPosterOrReadOnly]
    serializer_class = JobPostSerializer
    lookup_field = "slug"
    renderer_classes = [CustomRenderer]

    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(JobPost, slug=slug)  
        self.check_object_permissions(self.request, obj)
        return obj
    
    
class ApplyJobView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobApplicationSerializer
    renderer_classes = [CustomRenderer]
    
    def perform_create(self, serializer):
        slug = self.kwargs["slug"]
        job_post = JobPost.objects.get(slug=slug)
        job_application = JobApplication.objects.filter(job_post=job_post, applicant=self.request.user)
        
        if job_application.exists():
            raise ValidationError(
                                  {
                                    "status":"Error",
                                    "data": "You have already applied to this job post!"
                                  }
                                )
        serializer.save(job_post=job_post, applicant=self.request.user)
        job_post.no_of_applicants += 1
        job_post.save()    
        
        
class JobApplicationDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobApplicationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [JobApplicantOnly]
    renderer_classes = [CustomRenderer]
     
    
    def get_object(self):
        pk = self.kwargs["pk"]
        obj = get_object_or_404(JobApplication, id=pk)
        self.check_object_permissions(self.request, obj)
        return obj 
    
    def get_serializer_class(self):
        current_user = self.request.user
        serializer_class = self.serializer_class 
        
        if self.get_object().job_post.poster == current_user:
            serializer_class = JobApplicationSerializerForPoster
            
        return serializer_class
    

class JobApplicationListView(ListAPIView):
    serializer_class = JobApplicationSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["job_post__job_title", "review"]
    ordering_fields = ["applied_on"]
    pagination_class = CustomPagination 
    renderer_classes = [CustomRenderer]
    
    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user).order_by("applied_on")


        
    
    