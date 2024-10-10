from django.shortcuts import render
from .serializer import VideoSerializer
from .models import Video
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    