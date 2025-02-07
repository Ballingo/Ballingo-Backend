from rest_framework import viewsets
from .models import FoodItem
from .serializer import FoodItemSerializer

# Create your views here.

class FoodItemViewSet(viewsets.ModelViewSet):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()
