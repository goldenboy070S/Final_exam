from rest_framework.serializers import ModelSerializer
from .models import *

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'