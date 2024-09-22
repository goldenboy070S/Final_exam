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