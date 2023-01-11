from django.db import models
import uuid 
from django.utils import timezone
from auths.models import CustomUser
from django.utils.text import slugify 
from django.conf import settings
# Create your models here.


class JobPost(models.Model):
    CONTRACT_TYPE = (
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Freelance", "Freelance"),
        ("Internship", "Internship")
    )
    
    JOB_CATEGORY = (
        ("IT / SOftware development", "IT / SOftware development"),
        ("Design / UX", "Design / UX"),
        ("Marketing & Communication", "Marketing & Communication"),
        ("Finance", "Finance"),
        ("Operations & Support", "Operations & Support"),
        ("Other", "Other")
    )
    
    COMPANY_SIZE = (
        ("0-10", "0-10"),
        ("11-50", "11-50"),
        ("51-200", "51-200"),
        ("201-500", "201-500"),
        ("501-1000", "501-1000"),
        ("1001-5000", "1001-5000")
    )
    
    INDUSTRY = (
        ("SaaS", "SaaS"),
        ("E-commerce", "E-commerce"),
        ("Technology", "Technology"),
        ("Fashion", "Fashion"), 
        ("Finance", "Finance"),
        ("Health", "Health"), 
        ("Gaming", "Gaming"),
        ("Travel", "Travel"), 
        ("Food", "Food"),
        ("Education", "Education"),
        ("Transportation", "Transportation"),
        ("Music", "Music"), 
        ("Arts", "Arts"), 
        ("Others", "Others")
    )
    
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    company = models.CharField(max_length=70)
    logo = models.ImageField(upload_to="employers", null=True, blank=True)
    job_title = models.CharField(max_length=70)
    job_description = models.TextField()
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE)
    location = models.CharField(max_length=20)
    working_language = models.CharField(max_length=20)
    job_category = models.CharField(max_length=40, choices=JOB_CATEGORY)
    job_link = models.URLField(null=True, blank=True)
    email = models.EmailField()
    company_size = models.CharField(max_length=10, choices=COMPANY_SIZE)
    industry = models.CharField(max_length=25, choices=INDUSTRY)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    candidate_range = models.CharField(max_length=20, null=True, blank=True)
    questionnaire = models.JSONField(default=dict, null=True, blank=True)
    slug = models.SlugField(db_index=True, null=False)
    no_of_applicants = models.PositiveIntegerField(default=0)
    deadline = models.DateField(null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.job_title} needed at {self.company}, {self.slug}"
    
    
class JobApplication(models.Model):
    
    REVIEW_CHOICES = (
        ("accepted", "accepted"),
        ("rejected", "rejected")
    )
    
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="users", null=True, blank=True)
    cover_letter = models.TextField(null=True, blank=True)
    personality_note = models.CharField(max_length=200, null=True, blank=True)
    questionnaire_answers = models.JSONField(default=dict)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    applied_on = models.DateTimeField(default=timezone.now)
    review = models.CharField(max_length=15, choices=REVIEW_CHOICES, null=True)
    
    def __str__(self):
        return self.job_post.job_title 
    
    
    