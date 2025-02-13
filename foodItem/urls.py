from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'foodItem', views.FoodItemViewSet, basename='foodItem')

urlpatterns = router.urls

