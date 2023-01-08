from dashboard.models import JobPost
from rest_framework import serializers

class JobPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPost
        exclude = ["date_posted", "last_updated"]