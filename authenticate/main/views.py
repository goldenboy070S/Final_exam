from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# Create your views here.


class SportApiviewset(ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [DjangoModelPermissions]



class LeagueViewSet(ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [DjangoModelPermissions]



class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [DjangoModelPermissions]

    

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [DjangoModelPermissions]
  
