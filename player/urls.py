from django.urls import path, include
from .views import PlayerViewSet
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, GetPlayerByUserView

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')

# Agregar rutas adicionales sin afectar el router
urlpatterns = [
    path('players/by-user/<int:user_id>/', GetPlayerByUserView.as_view(), name='get_player_by_user'),
]

# Incluir las rutas del router
urlpatterns += router.urls