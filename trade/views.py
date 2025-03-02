from rest_framework import viewsets
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer

    def get_queryset(self):
        queryset = Trade.objects.all()
        is_active = self.request.query_params.get("isActive")

        if is_active is not None:
            # Convertir string a booleano correctamente
            if is_active.lower() in ["true", "1"]:
                queryset = queryset.filter(isActive=True)
            elif is_active.lower() in ["false", "0"]:
                queryset = queryset.filter(isActive=False)

        return queryset
