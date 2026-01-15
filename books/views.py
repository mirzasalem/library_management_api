from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from .models import Category, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import BookSerializer, LoginSerializer, RegisterSerializer
# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if not serializer.is_valid():
            return Response({'status' : 'False', 'msg' : serializer.errors}, status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save()
        return Response({'status' : 'True', 'msg' : 'User created successfully'}, status.HTTP_201_CREATED)



class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data)
            return Response({'Message' : 'Login Success'})
        return Response(serializer.errors)




class BooksAPI(APIView):


    def get(self, request):
        object = Book.objects.all()
        serializer = BookSerializer(object, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        
        
        
    
    
