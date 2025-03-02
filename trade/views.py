from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Trade
from .serializers import TradeSerializer
from foodItem.models import FoodItem
from foodList.models import FoodList
from player.models import Player  # Asegúrate de importar Player


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer

    def get_queryset(self):
        queryset = Trade.objects.all()
        is_active = self.request.query_params.get("isActive")

        if is_active is not None:
            # Convertir string a booleano correctamente
            if is_active.lower() in ["true", "1"]:
                queryset = queryset.filter(isActive=True)
            elif is_active.lower() in ["false", "0"]:
                queryset = queryset.filter(isActive=False)

        return queryset
    

    
    @action(detail=True, methods=['post'], url_path="accept")
    def accept_trade(self, request, pk=None):
        """Acepta un trade, intercambiando los alimentos entre jugadores."""
        try:
            trade = Trade.objects.get(pk=pk, isActive=True)

            player_offering = trade.player
            player_accepting_id = request.data.get("player_id")

            if not player_accepting_id:
                return Response({"error": "Se requiere player_id para aceptar el trade"}, status=status.HTTP_400_BAD_REQUEST)

            player_accepting = Player.objects.get(id=int(player_accepting_id))

            foodlist_offering = player_offering.inventory.food_inventory
            foodlist_accepting = player_accepting.inventory.food_inventory

            offered_food = FoodItem.objects.filter(foodlist=foodlist_offering, food=trade.in_food).first()
            requested_food = FoodItem.objects.filter(foodlist=foodlist_accepting, food=trade.out_food).first()

            if not offered_food:
                return Response({"error": "El jugador que ofrece no tiene el alimento ofrecido"}, status=status.HTTP_400_BAD_REQUEST)

            if not requested_food:
                return Response({"error": "El jugador que acepta no tiene el alimento solicitado"}, status=status.HTTP_400_BAD_REQUEST)

            offered_food.quantity -= 1
            if offered_food.quantity == 0:
                offered_food.delete()
            else:
                offered_food.save()

            requested_food.quantity -= 1
            if requested_food.quantity == 0:
                requested_food.delete()
            else:
                requested_food.save()

            accepted_food, created = FoodItem.objects.get_or_create(
                foodlist=foodlist_accepting,
                food=trade.in_food,
                defaults={"quantity": 1}
            )
            if not created:
                accepted_food.quantity += 1
                accepted_food.save()

            new_food, created = FoodItem.objects.get_or_create(
                foodlist=foodlist_offering,
                food=trade.out_food,
                defaults={"quantity": 1}
            )
            if not created:
                new_food.quantity += 1
                new_food.save()

            trade.isActive = False
            trade.save()

            return Response({"message": "Trade realizado con éxito"}, status=status.HTTP_200_OK)

        except Trade.DoesNotExist:
            return Response({"error": "Trade no encontrado o ya completado"}, status=status.HTTP_404_NOT_FOUND)

        except Player.DoesNotExist:
            return Response({"error": "El jugador que acepta no existe"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)