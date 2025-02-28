from player.models import Player
from foodList.models import FoodList
from foodItem.models import FoodItem

def add_food_to_list(player_id, food_id, quantity=1):
    player = Player.objects.get(id=player_id)
    food_list, created = FoodList.objects.get_or_create(player=player)

    food_item, created = FoodItem.objects.get_or_create(foodlist=food_list, food_id=food_id)
    food_item.quantity += quantity
    food_item.save()

    return f"Se agregaron {quantity} unidades de {food_item.food.name} a la lista de {player}. Cantidad total: {food_item.quantity}"
