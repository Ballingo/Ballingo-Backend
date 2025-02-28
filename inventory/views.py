from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from wardrobe.models import Wardrobe
from inventory.models import Inventory
from player.models import Player
from clothes.models import Clothes
from rest_framework.decorators import action
from wardrobe.serializers import WardrobeSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


    @action(detail=False, methods=['post'], url_path='add-clothes')
    def add_clothes(self, request):
        """
        Agrega una prenda de ropa al Wardrobe dentro del Inventory de un Player.
        """
        player_id = request.data.get('player_id')
        clothes_id = request.data.get('clothes_id')

        if not player_id or not clothes_id:
            return Response({"error": "Se requieren player_id y clothes_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory

            wardrobe = inventory.clothes_inventory

            clothes = Clothes.objects.get(id=int(clothes_id))

            wardrobe.items.add(clothes)

            return Response({"message": f"{clothes.type} añadido al wardrobe"}, status=status.HTTP_200_OK)

        except Player.DoesNotExist:
            return Response({"error": "Player no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory no encontrado para el Player"}, status=status.HTTP_404_NOT_FOUND)
        except Wardrobe.DoesNotExist:
            return Response({"error": "Wardrobe no encontrado en el Inventory"}, status=status.HTTP_404_NOT_FOUND)
        except Clothes.DoesNotExist:
            return Response({"error": "Prenda de ropa no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=['get'], url_path='get-wardrobe')
    def get_wardrobe(self, request, pk=None):
        """
        Obtiene el Wardrobe de un Player a partir de su player_id en la URL.
        """
        player_id = pk  # Ahora usamos `pk` en lugar de `query_params.get()`

        try:
            # Obtener el Player
            player = Player.objects.get(id=int(player_id))

            # Obtener el Inventory desde el Player
            inventory = player.inventory

            # Obtener el Wardrobe desde el Inventory
            wardrobe = inventory.clothes_inventory

            # Serializar y devolver el Wardrobe
            serializer = WardrobeSerializer(wardrobe)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Player.DoesNotExist:
            return Response({"error": "Player no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory no encontrado para el Player"}, status=status.HTTP_404_NOT_FOUND)
        except Wardrobe.DoesNotExist:
            return Response({"error": "Wardrobe no encontrado en el Inventory"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
