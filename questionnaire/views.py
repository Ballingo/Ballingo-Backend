from rest_framework import viewsets
from .models import Questionnaire
from .serializers import QuestionnaireSerializer
from language.models import Language
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    @action(detail=False, methods=['get'])
    def by_language(self, request):
        language_code = request.query_params.get("language_code")

        if not language_code:
            return Response({"error": "language_code is required"}, status=status.HTTP_400_BAD_REQUEST)

        language = get_object_or_404(Language, language=language_code)

        questionnaires = Questionnaire.objects.filter(language=language)

        serializer = QuestionnaireSerializer(questionnaires, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)