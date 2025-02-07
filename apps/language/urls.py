from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet

router = routers.DefaultRouter()
router.register(r'language', LanguageViewSet, "language")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
