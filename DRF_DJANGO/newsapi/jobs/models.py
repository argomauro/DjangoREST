from django.db import models

class Joboffer(models.Model):
    company_name = models.CharField(max_length=120, null=True, blank=True, default=None)
    company_email = models.EmailField(null=True, blank=True, default=None)
    job_title = models.CharField(max_length=120, null=True, blank=True, default=None)
    job_description = models.TextField(max_length=250, null=True, blank=True, default=None)
    salary = models.FloatField(null=True, blank=True, default=None)
    city = models.CharField(max_length=50, null=True, blank=True, default=None)
    state = models.CharField(max_length=20, null=True, blank=True, default=None)
    created_at = models.DateField(auto_now=True)
    available = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.company_name} - {self.job_title}'