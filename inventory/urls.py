from django.urls import path, include
from .views import InventoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = router.urls