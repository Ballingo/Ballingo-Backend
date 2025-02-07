from rest_framework import viewsets
from .models import FoodList
from .serializers import FoodListSerializer

# Create your views here.

class FoodListViewSet(viewsets.ModelViewSet):
    serializer_class = FoodListSerializer
    queryset = FoodList.objects.all()
