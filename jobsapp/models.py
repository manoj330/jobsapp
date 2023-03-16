from django.db import models

# Create your models here.
class WebCompanyJobs(models.Model):
    web_company_jobs_id = models.BigAutoField(primary_key=True)
    company_info_id = models.BigIntegerField()
    eligibility = models.CharField(max_length=1000, blank=True, null=True)
    job_title = models.CharField(max_length=1000, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_location = models.TextField(blank=True, null=True)
    apply_link = models.TextField(blank=True, null=True)
    posted_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    qualifications = models.TextField(blank=True, null=True)
    image_link=models.TextField(blank=True, null=True)
    
