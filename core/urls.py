from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

router = DefaultRouter()

router.register(r'audios', views.AudioViewset)
router.register(r'books', views.BookViewset)
router.register(r'links', views.LinkViewset)
router.register(r'videos', views.VideoViewset)

urlpatterns = [
    path('', include(router.urls)),
]