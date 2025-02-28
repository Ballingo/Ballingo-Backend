from rest_framework import viewsets
from .models import FoodItem
from .serializers import FoodItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class ReduceFoodQuantityView(APIView):
    def post(self, request):
        food_item_id = request.data.get("id")  # 🔹 Obtenemos el ID del FoodItem

        try:
            food_item = FoodItem.objects.get(id=food_item_id)  # 🔹 Buscamos el FoodItem

            if food_item.quantity > 0:
                food_item.quantity -= 1
                food_item.save()
                return Response({"message": "Cantidad actualizada", "new_quantity": food_item.quantity}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "No hay más unidades de este alimento"}, status=status.HTTP_400_BAD_REQUEST)

        except FoodItem.DoesNotExist:
            return Response({"error": "El alimento no existe"}, status=status.HTTP_404_NOT_FOUND)