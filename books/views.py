from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from .models import Category, Book, Bookrent
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated

from serializers.serializers import BookSerializer, LoginSerializer, RegisterSerializer, AddBookSerializer
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


class RentBookAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user
        if user.is_staff:
            return Response(
                {"error": "Staff members cannot rent books"},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        if book.available_copies <= 0:
            return Response(
                {"error": "No copies available"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Bookrent.objects.create(user=user, book=book)
        book.available_copies -= 1
        book.save()

        return Response(
            {"message": "Book rented successfully"},
            status=status.HTTP_200_OK
        )


class ReturnBookAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        user = request.user

        if user.is_staff:
            return Response(
                {"error": "Staff members cannot return books"},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            rent = Bookrent.objects.get(
                user=request.user, book_id=book_id, returned=False
            )
        except Bookrent.MultipleObjectsReturned:
            rent = Bookrent.objects.filter(book_id=book_id, user=user, returned=False).latest('rented_at') # multiple objects returned thats why used this.

        rent.returned = True
        rent.save()

        book = rent.book
        book.available_copies += 1
        book.save()
        

        return Response({'message': f'Book "{book.title}" returned successfully'})


class BooksAPI(APIView):


    def get(self, request):
        object = Book.objects.all()
        serializer = BookSerializer(object, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        
class AddBookAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = data)
        if not serializer.is_valid():
            return Response({'status' : 'False', 'msg' : serializer.errors}, status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save()
        return Response({'status' : 'True', 'msg' : 'Book created successfully'}, status.HTTP_201_CREATED)
    
    
