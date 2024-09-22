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
    def get(self, request: Request, pk=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self,request: Request, pk=None):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        return Response(CarSerializer(car).data)

    def put(self,request: Request, pk):
        try:
            car = Car.objects.get(id=pk)
        except Car.DoesNotExist:
            return Response({"message": "Car not found"})
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        return Response(CarSerializer(car).data)

    def delete(self,request: Request, pk):
        try:
            car = Car.objects.get(id=pk)
        except Car.DoesNotExist:
            return Response({"message": "Car not found"})
        car.delete()
        return Response({"message": "Car deleted successfully"})


class NewsAPI(APIView):
    def get(self, request: Request, pk=None):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)
    
    def post(self,request: Request, pk=None):
        serializer = NewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new = serializer.save()
        return Response(NewSerializer(new).data)
    
    def put(self,request: Request, pk):
        try:
            new = New.objects.get(id=pk)
        except New.DoesNotExist:
            return Response({"message": "News not found"})
        serializer = NewSerializer(new, data=request.data)
        serializer.is_valid(raise_exception=True)
        new = serializer.save()
        return Response(NewSerializer(new).data)
    
    def delete(self,request: Request, pk):
        try:
            new = New.objects.get(id=pk)
        except New.DoesNotExist:
            return Response({"message": "News not found"})
        new.delete()
        return Response({"message": "News deleted successfully"})
    

class ProductAPI(APIView):
    def get(self, request: Request, pk=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self,request: Request, pk=None):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return Response(ProductSerializer(product).data)
    
    def put(self,request: Request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'message': 'product not found'})
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        return Response(ProductSerializer(product).data)

    def delete(self,request: Request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'message': 'product not found'})
        product.delete()
        return Response({"message": "Product deleted successfully"})
    