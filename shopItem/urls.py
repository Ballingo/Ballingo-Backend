from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopItemViewSet

router = DefaultRouter()
router.register(f'shop-items', ShopItemViewSet, basename='shop-items')

urlpatterns = router.urls