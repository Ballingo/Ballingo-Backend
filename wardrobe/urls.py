from django.urls import path, include
from .views import WardrobeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wardrobe', WardrobeViewSet, basename='wardrobe')

urlpatterns = router.urls

