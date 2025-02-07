from rest_framework import viewsets
from .models import Questions
from .serializer import QuestionsSerializer

# Create your views here.

class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
