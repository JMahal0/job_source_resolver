from django.db import models

class JobDataModel(models.Model):
    id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_url = models.CharField(max_length=800)
    job_source = models.CharField(max_length=100)
