from rest_framework import viewsets
from .models import Questionnaire
from .serializers import QuestionnaireSerializer

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer