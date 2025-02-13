from django.urls import path, include
from .views import RealPackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'realPack', RealPackViewSet, basename='realPack')

urlpatterns = router.urls