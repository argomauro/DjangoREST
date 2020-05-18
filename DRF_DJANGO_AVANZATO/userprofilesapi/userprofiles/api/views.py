from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
#from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from userprofiles.models import Profile, StatusProfile
from userprofiles.api.serializers import ProfileSerializer, StatusProfileSerializer, ProfileAvatarSerializer
from userprofiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerProfileOrReadOnly

class ProfileViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, 
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    
class StatusProfileViewSet(viewsets.ModelViewSet):
    queryset = StatusProfile.objects.all()
    serializer_class = StatusProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly]
    
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
        
class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

