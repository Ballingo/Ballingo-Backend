from django.urls import path, include
from rest_framework import routers
from .views import CoinsShopViewSet

router = routers.DefaultRouter()
router.register(r'coins_shop', CoinsShopViewSet, "coins_shop")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
