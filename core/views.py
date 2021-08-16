from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class AudioViewset(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()

class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class LinkViewset(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

class VideoViewset(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
