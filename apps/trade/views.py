from rest_framework import viewsets
from .models import Trade
from .serializer import TradeSerializer

# Create your views here.

class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    queryset = Trade.objects.all()
