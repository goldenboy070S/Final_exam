from .models import *
from rest_framework.serializers import ModelSerializer

class SportSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class LeagueSerializer(ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    
class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        