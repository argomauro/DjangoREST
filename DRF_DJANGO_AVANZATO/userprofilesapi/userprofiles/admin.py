from django.contrib import admin
from userprofiles.models import Profile, StatusProfile
# Register your models here.
admin.site.register(Profile)
admin.site.register(StatusProfile)