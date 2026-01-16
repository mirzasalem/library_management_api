"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from books.views import BooksAPI , LoginAPI , RegisterAPI, RentBookAPI, ReturnBookAPI
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', BooksAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('rent/<int:book_id>/', RentBookAPI.as_view()),
    path('return/<int:book_id>/', ReturnBookAPI.as_view()),
    # path('library/', include('books.urls')),
]
