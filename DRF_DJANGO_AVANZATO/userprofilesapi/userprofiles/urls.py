from django.urls import path, include
from userprofiles.api.views import ProfileViewSet, StatusProfileViewSet, AvatarUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', StatusProfileViewSet, basename='status')


urlpatterns = [
   path('', include(router.urls)),
   path('avatar/',AvatarUpdateView.as_view(), name='avatar-update')

]

'''
CONFIGURAZIONE SENZA ROUTERS

profile_list = ProfileViewSet.as_view({'get':'list'})
profile_detail = ProfileViewSet.as_view({'get':'retrieve'})

urlpatterns = [
    path('list/', profile_list, name='profile-list'),
    path('list/<int:pk>', profile_detail, name='profile-detail'),

]

'''