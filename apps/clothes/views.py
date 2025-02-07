from rest_framework import viewsets
from .models import Clothes
from .serializer import ClothesSerializer

# Create your views here.

class ClothesViewSet(viewsets.ModelViewSet):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()