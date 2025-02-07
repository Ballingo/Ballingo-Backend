from rest_framework import viewsets
from .models import Language
from .serializer import LanguageSerializer

# Create your views here.

class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
