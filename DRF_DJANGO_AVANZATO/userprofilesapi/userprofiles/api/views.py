from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.filters import SearchFilter
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
    filter_backends = [SearchFilter]
    search_fields = ['city']
    
class StatusProfileViewSet(viewsets.ModelViewSet):
    serializer_class = StatusProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly]
    
    def get_queryset(self):
        queryset = StatusProfile.objects.all()
        username = self.request.query_params.get('username',None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset
    
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
        
class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

