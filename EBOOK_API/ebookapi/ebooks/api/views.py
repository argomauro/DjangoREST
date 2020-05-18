from rest_framework import mixins, generics, permissions
from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer
from django.shortcuts import get_object_or_404
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from rest_framework.exceptions import ValidationError
from ebooks.api.pagination import EbooksPaginations

#VIEW CREATA A MANO UTILIZANDO LA GENERIC APIVIEW
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
    queryset = Ebook.objects.all().order_by("publication_date")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = EbooksPaginations


class EbookDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    '''
    APIVIEW DETAIL CON UTILIZZO DEI GENERICS
    '''
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateApiview(generics.CreateAPIView):
    '''
    APIVIEW CREATE REVIEW CON UTILIZZO DEI GENERICS
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        author_user = self.request.user
        review_exist = Review.objects.filter(ebook=ebook,author_user=author_user).exists()
        if review_exist:
            raise ValidationError('Hai già recensito questo libro')
        serializer.save(ebook=ebook, author_user=author_user)

class ReviewDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    '''
    APIVIEW DETAIL REVIEW CON UTILIZZO DEI GENERICS
    '''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    