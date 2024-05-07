from django.urls import path, include
from rest_framework import routers
from .views import SongViewSet, PlaylistViewSet

router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]