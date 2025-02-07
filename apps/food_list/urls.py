from django.urls import path, include
from rest_framework import routers
from .views import FoodListViewSet

router = routers.DefaultRouter()
router.register(r'food_list', FoodListViewSet, "food_list")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
