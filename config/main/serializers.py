from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class Cars:
    def __init__(self, model, description, created_at, updated_at, image):
        self.model = model
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.image = image


class CarSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=150)  
    description = serializers.CharField()  
    created_at = serializers.DateTimeField()  
    updated_at = serializers.DateTimeField()
    image = serializers.ImageField()  

    def create(self, validated_data):
        return Cars(**validated_data)  

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.image = validated_data.get('image', instance.image) 
        return instance


class NewSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
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