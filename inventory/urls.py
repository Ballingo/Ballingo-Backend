from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, GetPlayerLivesCounter, UpdatePlayerLivesCounter, UpdatePlayerWardrobe

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
    path('inventory/get-lives/<int:player_id>/', GetPlayerLivesCounter.as_view(), name='get-lives'),
    path('inventory/set-lives/<int:player_id>/', UpdatePlayerLivesCounter.as_view(), name='update-lives'),
    path('inventory/set-wardrobe/<int:player_id>/', UpdatePlayerWardrobe.as_view(), name='update-wardrobe'),
]
