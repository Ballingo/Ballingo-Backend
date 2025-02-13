from rest_framework import viewsets
from .models import Wardrobe
from .serializers import WardrobeSerializer

class WardrobeViewSet(viewsets.ModelViewSet):
    queryset = Wardrobe.objects.all()
    serializer_class = WardrobeSerializer