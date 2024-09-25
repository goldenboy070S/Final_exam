from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class CarSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=150)  
    description = serializers.CharField()  
    created_at = serializers.DateTimeField()  
    updated_at = serializers.DateTimeField()  

    def create(self, validated_data):
        return Car.objects.create(**validated_data)  

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


class NewSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return New.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    author_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class MoviewSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    author_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    description = serializers.CharField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Moview.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    author_id = serializers.IntegerField()
    move_id = serializers.IntegerField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.author = validated_data.get('author', instance.author)
        instance.move = validated_data.get('movie', instance.move)
        instance.save()
        return instance
    

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance








# def convert_to_json():
#     serializer = CarSerializer(car)
#     print(serializer.data)
#     json = JSONRenderer().render(serializer.data)
#     print(json)

# def json_to_python():
#     json = b'{"model":"nimadur nima","description":"biror narsa yoki narsa"}'
#     steam = io.BytesIO(json)
#     data = JSONParser().parse(steam)
#     serializer = CarSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)