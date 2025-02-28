from django.urls import path
from .views import FoodListView, AddFoodToListView, GetFoodListByPlayerView

urlpatterns = [
    path('food-lists/', FoodListView.as_view(), name='food_list'), 
    path('add-food/', AddFoodToListView.as_view(), name='add_food_to_list'),
    path('food-list/<int:player_id>/', GetFoodListByPlayerView.as_view(), name='get_food_list_by_player'),  # Nueva ruta
]