from rest_framework import mixins, generics
from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer
from django.shortcuts import get_object_or_404

class EbookListCreate(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EbookListCreateApiview(generics.ListCreateAPIView):
    '''
    APIVIEW LIST CON UTILIZZO DEI GENERICS
    '''
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    '''
    APIVIEW DETAIL CON UTILIZZO DEI GENERICS
    '''
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class ReviewCreateApiview(generics.CreateAPIView):
    '''
    APIVIEW CREATE REVIEW CON UTILIZZO DEI GENERICS
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        print('EBOOK_PK',ebook_pk)
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)

class ReviewDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    '''
    APIVIEW DETAIL REVIEW CON UTILIZZO DEI GENERICS
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    