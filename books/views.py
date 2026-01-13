from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from .models import Category, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import BookSerializer
# Create your views here.

class BooksAPI(APIView):


    def get(self, request):
        object = Book.objects.all()
        serializer = BookSerializer(object, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message' : 'This is a get request'})
    
    
