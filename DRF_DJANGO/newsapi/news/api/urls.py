from django.urls import path
from news.api.views import (article_list_create_api_view, 
                            article_detail_api_view,
                            ArticleListCreaterAPIView,
                            ArticleDetailAPIView,
                            JournalistListCreaterAPIView)

urlpatterns = [
    path('articles/',
         article_list_create_api_view, 
         name='article_list'),
    
    path('articles/<int:pk>/', 
         article_detail_api_view, 
         name='article_detail'),
    
    path('articles/apiview/',
         ArticleListCreaterAPIView.as_view(), 
         name='article_list_apiview'),
    
    path('articles/apiview/<int:pk>/', 
         ArticleDetailAPIView.as_view(), 
         name='article_detail_apiview'),
    
    path('journalists/apiview/',
         JournalistListCreaterAPIView.as_view(), 
         name='journalist_list_apiview'),

]