from rest_framework import serializers
from books.models import Book, Category
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")
    
    
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only= True)
    role = serializers.ChoiceField(
        choices=[('student', 'Student'), ('staff', 'Staff')],
        default='student'
    )
    class Meta:
        model = User
        fields = ['username','email', 'password', 'role']

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username Already Exists')
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError('Email Already Exists')
        return data

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create(username = validated_data['username'], email = validated_data['email'], is_staff=True if role == 'staff' else False)
        user.set_password(validated_data['password'])
       
        user.save()
        return user
        # print("Saved")
        # return super().create(validated_data)
    
    
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        


        
class AddBookSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only= True)
    role = serializers.ChoiceField(
        choices=[('student', 'Student'), ('staff', 'Staff')],
        default='student'
    )
    class Meta:
        model = User
        fields = ['username','email', 'password', 'role']

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username Already Exists')
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError('Email Already Exists')
        return data

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create(username = validated_data['username'], email = validated_data['email'], is_staff=True if role == 'staff' else False)
        user.set_password(validated_data['password'])
       
        user.save()
        return user