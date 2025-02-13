from django.urls import path, include
from .views import TradeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trade', TradeViewSet, basename='trade')

urlpatterns = router.urls
