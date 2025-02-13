from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerProgressViewSet

router = DefaultRouter()
router.register(r'player-progress', PlayerProgressViewSet, basename='player-progress')

urlpatterns = router.urls