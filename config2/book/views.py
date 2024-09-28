from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,
                                      DestroyAPIView, UpdateAPIView, ListCreateAPIView,
                                        RetrieveUpdateAPIView, RetrieveDestroyAPIView) 
from .models import * 
from .serializers import *
# Create your views here.


class BookApi(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorApi(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreApi(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class DetailBookApi(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailAuthorApi(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class DetailGenreApi(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
