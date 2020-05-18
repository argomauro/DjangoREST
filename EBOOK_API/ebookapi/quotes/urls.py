from django.urls import path, include
from quotes.api.views import QuoteListCreateAPIView, QuoteDetailApiview
urlpatterns = [
    path('quotes/',QuoteListCreateAPIView.as_view() ,name='quote_list'),
    path('quote/<int:pk>',QuoteDetailApiview.as_view() ,name='quote_detail'),
]