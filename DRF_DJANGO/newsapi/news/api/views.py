from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer



#ClassView
class ArticleListCreaterAPIView(APIView):
    '''
    Mostra un elenco degli articoli presenti nel DBMS e ne crea uno
    nuovo con metodo POST
    '''
    def get(self, request):
        #articles = Article.objects.filter(active=True)
        #alternativa è quella di chiamare un altro metodo
        articles = get_list_or_404(Article, active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    '''
    Mostra un dettaglio di articolo presenti nel DBMS 
    è possibile farsi restituire un oggetto, modificarlo o cancellarlo
    '''
    def get_object(self, pk):
        article = get_object_or_404(Article,pk=pk)
        return article
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self,request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#ClassView
class JournalistListCreaterAPIView(APIView):
    '''
    Mostra un elenco degli articoli presenti nel DBMS e ne crea uno
    nuovo con metodo POST
    '''
    def get(self, request):
        #articles = Article.objects.filter(active=True)
        #alternativa è quella di chiamare un altro metodo
        journalists = get_list_or_404(Journalist)
        serializer = JournalistSerializer(journalists, many=True,
                                          context={'request':request} )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#Metodi
@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api_view(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({'Error': {
            'code': 404,
            'message': 'Articolo non trovato'
        }
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
