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
from rest_framework.views import APIView

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
        player_id = pk

        try:
            player = Player.objects.get(id=int(player_id))

            inventory = player.inventory

            wardrobe = inventory.clothes_inventory

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
    
    @action(detail=True, methods=['get'], url_path='get-coins')
    def get_player_coins(self, request, pk=None):
        player_id = pk

        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory
            coins = inventory.coins

            return Response({"coins": coins}, status=status.HTTP_200_OK)
        
        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['put'], url_path='update-coins')
    def update_player_coins(self, request, pk=None):
        player_id = pk
        amount = request.data.get('coins')

        try:
            amount = int(amount)
        except (TypeError, ValueError):
            return Response({"error": "Invalid value for 'coins'. It must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory

            new_coins = inventory.coins + amount

            if new_coins < 0:
                return Response({"error": "Not enough coins."}, status=status.HTTP_400_BAD_REQUEST)

            inventory.coins = new_coins
            inventory.save()

            return Response({"message": "Succes", "New_balance": inventory.coins}, status=status.HTTP_200_OK)

        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)

class GetPlayerLivesCounter(APIView):
    def get(self, request, player_id):
        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory
            lives_counter = inventory.livesCounter

            return Response({"lives_counter": lives_counter}, status=status.HTTP_200_OK)
        
        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdatePlayerLivesCounter(APIView):
    def put(self, request, player_id):
        amount = request.data.get('lives_counter')

        try:
            amount = int(amount)
        except (TypeError, ValueError):
            return Response({"error": "Invalid value for 'lives_counter'. It must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory

            new_lives_counter = inventory.livesCounter + amount

            if new_lives_counter < 0:
                return Response({"error": "Not enough lives."}, status=status.HTTP_400_BAD_REQUEST)

            inventory.livesCounter = new_lives_counter
            inventory.save()

            return Response({"message": "Succes", "New_lives_counter": inventory.livesCounter}, status=status.HTTP_200_OK)

        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)

class ChangeLivesAfterDeath(APIView):
    def put(self, request, player_id):
        amount = request.data.get('lives_counter')
        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory

            if amount < 0:
                return Response({"error": "Not enough lives."}, status=status.HTTP_400_BAD_REQUEST)

            inventory.livesCounter = amount
            inventory.save()

            return Response({"message": "Succes", "New_lives_counter": inventory.livesCounter}, status=status.HTTP_200_OK)

        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdatePlayerWardrobe(APIView):
    def put(self, request, player_id):
        clothes_id = request.data.get('clothes_id')

        try:
            clothes = Clothes.objects.get(id=int(clothes_id))
        except Clothes.DoesNotExist:
            return Response({"error": "Clothes not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            player = Player.objects.get(id=int(player_id))
            inventory = player.inventory
            wardrobe = inventory.clothes_inventory

            wardrobe.items.add(clothes)

            return Response({"message": f"{clothes.type} added to the wardrobe"}, status=status.HTTP_200_OK)

        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        except Wardrobe.DoesNotExist:
            return Response({"error": "Wardrobe not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
