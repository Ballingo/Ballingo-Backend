from django.urls import path, include
from .views import ClothesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clothes', ClothesViewSet, basename='clothes')

urlpatterns = router.urls