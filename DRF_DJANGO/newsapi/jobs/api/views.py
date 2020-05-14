from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404

from jobs.models import Joboffer
from jobs.api.serializers import JobsSerializer

#ClassView
class JobsListCreaterAPIView(APIView):
    '''
    Mostra un elenco delle offerte di lavoro presenti nel DBMS e ne crea uno
    nuovo con metodo POST
    '''
    def get(self, request):
        joboffers = get_list_or_404(Joboffer)
        serializer = JobsSerializer(joboffers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class JobsDetailAPIView(APIView):
    '''
    Mostra un dettaglio di un lavoro presenti nel DBMS 
    è possibile farsi restituire un oggetto, modificarlo o cancellarlo
    è anche possibile fare un aggiornamento parziale
    '''
    def get_object(self, pk):
        joboffer = get_object_or_404(Joboffer,pk=pk)
        return joboffer
    
    def get(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobsSerializer(joboffer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobsSerializer(joboffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    # set partial=True to update a data partially
    def patch(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobsSerializer(joboffer, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk):
        joboffer = self.get_object(pk)
        joboffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)