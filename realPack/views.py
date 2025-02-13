from rest_framework import viewsets
from .models import RealPack
from .serializers import RealPackSerializer

class RealPackViewSet(viewsets.ModelViewSet):
    queryset = RealPack.objects.all()
    serializer_class = RealPackSerializer
