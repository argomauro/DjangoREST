from django.urls import path
from ebooks.api.views import (EbookListCreate, 
                              EbookListCreateApiview,
                              EbookDetailApiview,ReviewSerializer,
                              ReviewCreateApiview,
                              ReviewDetailApiview)

urlpatterns = [
    #path('ebooks/', EbookListCreate.as_view(),
    #    name='ebook_list' ),
    path('ebooks/', EbookListCreateApiview.as_view(),
         name='ebook_list' ),
    path('ebook/<int:pk>', EbookDetailApiview.as_view(),
         name='ebook_detail' ),
    path('ebook/<int:ebook_pk>/review', ReviewCreateApiview.as_view(),
         name='ebook_detail_review' ),
    path('review/<int:pk>', ReviewDetailApiview.as_view(),
         name='review_detail' ),
]