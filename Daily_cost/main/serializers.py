from .models import Daily_cost
from rest_framework.serializers import ModelSerializer


class Daily_costSerializer(ModelSerializer):
    class Meta:
        model = Daily_cost
        fields = '__all__'
        