from django.urls import path, include
from rest_framework import routers
from .views import FoodViewSet

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet)

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('food/', include(router.urls)),
]
