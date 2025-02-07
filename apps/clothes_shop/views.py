from rest_framework import viewsets
from .models import ClothesShop
from .serializer import ClothesShopSerializer

# Create your views here.

class ClothesShopViewSet(viewsets.ModelViewSet):
    serializer_class = ClothesShopSerializer
    queryset = ClothesShop.objects.all()
