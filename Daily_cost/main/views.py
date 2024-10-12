from django.shortcuts import render
from .models import Daily_cost
from rest_framework.viewsets import ModelViewSet
from .serializers import Daily_costSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.


class Daily_costViewSet(ModelViewSet):
    queryset = Daily_cost.objects.all()
    serializer_class = Daily_costSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
