from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.models import Quote
from quotes.api.serializers import QuotesSerializer
from quotes.api.pagination import QuotePagination

class QuoteListCreateAPIView(ListCreateAPIView):
    queryset = Quote.objects.all().order_by("created_at")
    serializer_class = QuotesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = QuotePagination
    
class QuoteDetailApiview(RetrieveUpdateDestroyAPIView):
    '''
    APIVIEW DETAIL CON UTILIZZO DEI GENERICS
    '''
    queryset = Quote.objects.all().order_by("created_at")
    serializer_class = QuotesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = QuotePagination
