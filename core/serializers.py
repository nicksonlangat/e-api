from rest_framework import serializers
from .models import *

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields=[
            'id',
            'title',
            'file'
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=[
            'id',
            'title',
            'image',
            'author',
            'description',
            'file'
        ]

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields=[
            'id',
            'title',
            'file'
        ]


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields=[
            'id',
            'title',
            'link',
        ]


