from django.urls import path, include
from rest_framework import routers
from .views import PlayerProgressViewSet

router = routers.DefaultRouter()
router.register(r'player_progress', PlayerProgressViewSet, "player_progress")

# This generates the URLs for GET/POST/PUT/DELETE
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
