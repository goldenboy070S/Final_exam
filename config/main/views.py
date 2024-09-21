from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.


class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIdetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPI(APIView):
    def get(self, request: Request):
        cars = Car.objects.all()
        car = CarSerializer(cars, many=True)
        return Response(car.data)


class NewsAPI(APIView):
    def get(self, request: Request):
        news = New.objects.all()
        new = NewSerializer(news, many=True)
        return Response(new.data)
    

class ProductAPI(APIView):
    def get(self, request: Request):
        products = Product.objects.all()
        pro = []
        for i in products:
            pro.append({'id': i.id,
                        'name': i.name,
                        'description': i.description,
                        'created_at': i.created_at,
                        'image': i.image.url})
        return Response(pro)