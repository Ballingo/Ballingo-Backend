from django.urls import path, include
from rest_framework import routers
from .views import TradeViewSet

router = routers.DefaultRouter()
router.register(r'trade', TradeViewSet, "trade")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
