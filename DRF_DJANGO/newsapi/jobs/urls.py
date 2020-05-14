from django.urls import path
from jobs.api.views import JobsListCreaterAPIView, JobsDetailAPIView

urlpatterns = [
    path('list/',
         JobsListCreaterAPIView.as_view(), 
         name='jobs-list'),
    path('detail/<int:pk>',
         JobsDetailAPIView.as_view(), 
         name='jobs-detail'),
]