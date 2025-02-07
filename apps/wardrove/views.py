from rest_framework import viewsets
from .models import Wardrove
from .serializer import WardroveSerializer

# Create your views here.

class WardroveViewSet(viewsets.ModelViewSet):
    serializer_class = WardroveSerializer
    queryset = Wardrove.objects.all()
