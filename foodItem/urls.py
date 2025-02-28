from django.urls import path, include
from .views import FoodItemViewSet, ReduceFoodQuantityView  # 🔹 Importamos la nueva vista
from rest_framework.routers import DefaultRouter

# Registrar el ViewSet en el router
router = DefaultRouter()
router.register(r'foodItem', FoodItemViewSet, basename='foodItem')

# Agregar rutas adicionales sin afectar el router
urlpatterns = [
    path("reduce-food/", ReduceFoodQuantityView.as_view(), name="reduce_food_quantity"),
]

# Incluir las rutas del router
urlpatterns += router.urls
