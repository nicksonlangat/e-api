from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length = 150)
    file = models.FileField(upload_to='videos')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

class Book(models.Model):
    title = models.CharField(max_length = 150)
    file = models.FileField(upload_to='books')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    author = models.CharField( blank=True, null=True,  max_length = 150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

class Audio(models.Model):
    title = models.CharField(max_length = 150)
    file = models.FileField(upload_to='books')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

class Link(models.Model):
    title = models.CharField(max_length = 150)
    link = models.URLField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)
    
    
    
    