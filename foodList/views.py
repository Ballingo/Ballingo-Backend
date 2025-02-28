from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FoodList
from .serializers import FoodListSerializer
from foodList.services import add_food_to_list

class FoodListView(generics.ListCreateAPIView):
    queryset = FoodList.objects.all()
    serializer_class = FoodListSerializer 

class AddFoodToListView(APIView):
    def post(self, request):
        player_id = request.data.get('player_id')
        food_id = request.data.get('food_id')
        quantity = request.data.get('quantity', 1)

        if not player_id or not food_id:
            return Response({"error": "Se requieren player_id y food_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            message = add_food_to_list(player_id=int(player_id), food_id=int(food_id), quantity=int(quantity))
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class GetFoodListByPlayerView(APIView):
    def get(self, request, player_id):
        try:
            food_list = FoodList.objects.get(player_id=player_id)  # Obtener la lista del jugador
            serializer = FoodListSerializer(food_list)  # Serializar con los alimentos incluidos
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FoodList.DoesNotExist:
            return Response({"error": "No se encontró una lista de comida para este jugador."}, status=status.HTTP_404_NOT_FOUND)
