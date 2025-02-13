from django.urls import path, include
from .views import GamePackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gamePack', GamePackViewSet, basename='gamePack')

urlpatterns = router.urls