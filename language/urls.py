from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet

router = DefaultRouter()

router.register(r'language', LanguageViewSet, basename='language')

urlpatterns = router.urls
