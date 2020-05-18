from rest_framework import serializers
from userprofiles.models import Profile, StatusProfile

class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    avatar = serializers.ImageField(read_only=True)
    
    class Meta:
        model=Profile
        fields = '__all__'

class ProfileAvatarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Profile
        fields = ['avatar',]

class StatusProfileSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=StatusProfile
        fields = '__all__'