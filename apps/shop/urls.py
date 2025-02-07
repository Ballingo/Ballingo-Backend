from django.urls import path, include
from rest_framework import routers
from .views import ShopViewSet

router = routers.DefaultRouter()
router.register(r'shop', ShopViewSet, "shop")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
