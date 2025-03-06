from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import PlayerProgress
from .serializers import PlayerProgressSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from player.models import Player
from questionnaire.models import Questionnaire
from language.models import Language

class PlayerProgressViewSet(viewsets.ModelViewSet):
    queryset = PlayerProgress.objects.all()
    serializer_class = PlayerProgressSerializer

    @action(detail=False, methods=['post'])
    def create_progress(self, request):
        """
        Crea un PlayerProgress para un player y un language específico en nivel 1.
        """
        player_id = request.data.get('player_id')
        language_code = request.data.get('language_code')
        level = request.data.get('level')

        if not player_id or not language_code:
            return Response({"error": "Se requieren player_id y language_code"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            player = Player.objects.get(id=player_id)
        except Player.DoesNotExist:
            return Response({"error": "Player no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        try:
            language = Language.objects.get(language=language_code)  # Suponiendo que Language tiene un campo 'code'
        except Language.DoesNotExist:
            return Response({"error": "Idioma no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        try:
            questionnaire = Questionnaire.objects.get(language=language, level=level)
        except Questionnaire.DoesNotExist:
            return Response({"error": "Cuestionario no encontrado para este idioma y nivel"}, status=status.HTTP_404_NOT_FOUND)

        # Verificar si ya existe un PlayerProgress para este player y cuestionario
        if PlayerProgress.objects.filter(player=player, questionnaire=questionnaire).exists():
            return Response({"error": "El progreso ya existe para este cuestionario"}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el progreso
        player_progress = PlayerProgress.objects.create(player=player, questionnaire=questionnaire)
        serializer = PlayerProgressSerializer(player_progress)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def get_progress(self, request):
        player_id = request.query_params.get('player_id')
        language_code = request.query_params.get('language_code')

        if not player_id or not language_code:
            return Response({"error": "player_id and language_code are required"}, status=status.HTTP_400_BAD_REQUEST)

        player = get_object_or_404(Player, id=player_id)

        language = get_object_or_404(Language, language=language_code)

        player_progresses = PlayerProgress.objects.filter(player=player, questionnaire__language=language)

        if not player_progresses.exists():
            return Response({"error": "Player progress not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerProgressSerializer(player_progresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def get_levels(self, request):
        """
        Obtiene los niveles (PlayerProgress) de un jugador en un idioma específico.
        """
        player_id = request.data.get('player_id')
        language_code = request.data.get('language_code')

        if not player_id or not language_code:
            return Response({"error": "Se requieren player_id y language_code"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            player = Player.objects.get(id=player_id)
        except Player.DoesNotExist:
            return Response({"error": "Player no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        try:
            language = Language.objects.get(language=language_code)
        except Language.DoesNotExist:
            return Response({"error": "Idioma no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Obtener los cuestionarios en el idioma especificado
        questionnaires = Questionnaire.objects.filter(language=language)

        # Obtener los PlayerProgress asociados al player y a esos cuestionarios
        player_progress = PlayerProgress.objects.filter(player=player, questionnaire__in=questionnaires)

        # Serializar y devolver los datos
        serialized_data = PlayerProgressSerializer(player_progress, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)