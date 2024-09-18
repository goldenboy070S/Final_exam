from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
# Create your views here.



class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIdetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer