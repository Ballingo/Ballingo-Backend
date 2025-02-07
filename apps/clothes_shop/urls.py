from django.urls import path, include
from rest_framework import routers
from .views import ClothesShopViewSet

router = routers.DefaultRouter()
router.register(r'clothes_shop', ClothesShopViewSet, "clothes_shop")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
