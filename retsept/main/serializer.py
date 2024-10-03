from rest_framework.serializers import ModelSerializer
from .models import *

class ReteptSerializer(ModelSerializer):
    class Meta:
        model = Retsept
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        