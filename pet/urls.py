from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet

router = DefaultRouter()
router.register(r'pet', PetViewSet)

urlpatterns = [
    # Ruta personalizada para obtener una mascota por player_id y language
    path('pet/by-player/', PetViewSet.as_view({'get': 'get_pet_by_player_and_language'}), name='get_pet_by_player_and_language'),
]

# Agregar las rutas del router automáticamente generadas
urlpatterns += router.urls