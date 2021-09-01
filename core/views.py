from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AudioViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()

class BookViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class LinkViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

class VideoViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
