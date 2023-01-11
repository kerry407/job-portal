from dashboard.models import JobPost, JobApplication
from rest_framework import serializers

class JobPostSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    
    def get_poster(self, obj):
        return obj.poster.email
    class Meta:
        model = JobPost
        exclude = ["date_posted", "last_updated", "slug"]
        

class JobApplicationSerializer(serializers.ModelSerializer):
    job_review = serializers.SerializerMethodField()
    
    def get_job_review(self, obj):
        return obj.review
    class Meta:
        model = JobApplication
        exclude = ["job_post", "review"]
    

class JobApplicationSerializerForPoster(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        exclude = ["job_post"]