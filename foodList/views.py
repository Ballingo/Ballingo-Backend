from rest_framework import viewsets
from .models import FoodList
from .serializers import FoodListSerializer

class FoodListViewSet(viewsets.ModelViewSet):
    queryset = FoodList.objects.all()
    serializer_class = FoodListSerializer
    
