from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView

from ..models import JobPost
from .serializers import JobPostSerializer


class CreateJobPostView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobPostSerializer
    
    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(poster=user)
        
            