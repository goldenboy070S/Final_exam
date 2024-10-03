from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
# Create your views here.


class ReteptViewSet(ModelViewSet):
    queryset = Retsept.objects.all()
    serializer_class = ReteptSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
