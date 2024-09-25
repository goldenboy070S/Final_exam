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
    

class BookAPI(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                return Response(BookSerializer(book).data)
            except Book.DoesNotExist:
                return Response({"message": "Book not found"})
        books = Book.objects.all()
        return Response(BookSerializer(books, many=True).data)
    
    def post(self, request: Request, pk=None):
        if not pk:
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            book = serializer.save()
            return Response(BookSerializer(book).data)
        else:
            return Response({"message": "Method POST not allowed"})
        
    def put(self, request: Request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                serializer = BookSerializer(book, data=request.data)
                serializer.is_valid(raise_exception=True)
                book = serializer.save()
                return Response(BookSerializer(book).data)
            except Book.DoesNotExist:
                return Response({"message": "Book not found"})
        else:
            return Response({"message": "Method PUT not allowed"})
        
    def delete(self, request: Request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                book.delete()
                return Response({"message": "Book deleted successfully"})
            except Book.DoesNotExist:
                return Response({"message": "Book not found"})
        else:
            return Response({"message": "Method DELETE not allowed"})


class MoviewApi(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                movie = Moview.objects.get(pk=pk)
                return Response(MoviewSerializer(movie).data)
            except Moview.DoesNotExist:
                return Response({"message": "Movie not found"})
        movies = Moview.objects.all()
        return Response(MoviewSerializer(movies, many=True).data)
    
    def post(self, request: Request, pk=None):
        if not pk:
            serializer = MoviewSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            movie = serializer.save()
            return Response(MoviewSerializer(movie).data)
        else:
            return Response({"message": "Method POST not allowed"})
        
    def put(self, request: Request, pk=None):
        if pk:
            try:
                movie = Moview.objects.get(pk=pk)
                serializer = MoviewSerializer(movie, data=request.data)
                serializer.is_valid(raise_exception=True)
                movie = serializer.save()
                return Response(MoviewSerializer(movie).data)
            except Moview.DoesNotExist:
                return Response({"message": "Movie not found"})
        else:
            return Response({"message": "Method PUT not allowed"})
        
    def delete(self, request: Request, pk=None):
        if pk:
            try:
                movie = Moview.objects.get(pk=pk)
                movie.delete()
                return Response({"message": "Movie deleted successfully"})
            except Moview.DoesNotExist:
                return Response({"message": "Movie not found"})
        else:
            return Response({"message": "Method DELETE not allowed"})
    

class CommentAPI(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                return Response(CommentSerializer(comment).data)
            except Comment.DoesNotExist:
                return Response({"message": "Comment not found"})
        comments = Comment.objects.all()
        return Response(CommentSerializer(comments, many=True).data)
    
    def post(self, request: Request, pk=None):
        if not pk:
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            comment = serializer.save()
            return Response(CommentSerializer(comment).data)
        else:
            return Response({"message": "Method POST not allowed"})
        
    def put(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(comment, data=request.data)
                serializer.is_valid(raise_exception=True)
                comment = serializer.save()
                return Response(CommentSerializer(comment).data)
            except Comment.DoesNotExist:
                return Response({"message": "Comment not found"})
        else:
            return Response({"message": "Method PUT not allowed"})
    
    def delete(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                comment.delete()
                return Response({"message": "Comment deleted successfully"})
            except Comment.DoesNotExist:
                return Response({"message": "Comment not found"})
        else:
            return Response({"message": "Method DELETE not allowed"})
        

class CategoryAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                return Response(CategorySerializer(category).data)
            except Category.DoesNotExist:
                return Response({"message": "Category not found"})
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)
    
    def post(self, request, pk=None):
        if not pk:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            category = serializer.save()
            return Response(CategorySerializer(category).data)
        else:
            return Response({"message": "Method POST not allowed"})
        
    def put(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category, data=request.data)
                serializer.is_valid(raise_exception=True)
                category = serializer.save()
                return Response(CategorySerializer(category).data)
            except Category.DoesNotExist:
                return Response({"message": "Category not found"})
        else:
            return Response({"message": "Method PUT not allowed"})
        
    def delete(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                category.delete()
                return Response({"message": "Category deleted successfully"})
            except Category.DoesNotExist:
                return Response({"message": "Category not found"})
        else:
            return Response({"message": "Method DELETE not allowed"})   







