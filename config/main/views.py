from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
# Create your views here.



class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


