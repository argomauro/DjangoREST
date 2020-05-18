from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=80, blank=True)
    avatar = models.ImageField(null=True, blank=True)
# Create your models here.

    def __str__(self):
        return f'{self.user.username} - {self.city}'

class StatusProfile(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
# Create your models here.

    class Meta:
        verbose_name_plural = 'statuses'
        
    def __str__(self):
        return str(self.user_profile)