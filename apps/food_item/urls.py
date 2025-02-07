from django.urls import path, include
from rest_framework import routers
from .views import FoodItemViewSet

router = routers.DefaultRouter()
router.register(r'food_item', FoodItemViewSet, "food_item")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
