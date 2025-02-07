from rest_framework import viewsets
from .models import CoinsShop
from .serializer import CoinsShopSerializer

# Create your views here.

class CoinsShopViewSet(viewsets.ModelViewSet):
    serializer_class = CoinsShopSerializer
    queryset = CoinsShop.objects.all()
