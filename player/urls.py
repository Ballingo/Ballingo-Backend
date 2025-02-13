from django.urls import path, include
from .views import PlayerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')

urlpatterns = router.urls