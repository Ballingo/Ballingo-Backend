import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Pet
from .serializers import PetSerializer
from clothes.models import Clothes
from django.shortcuts import get_object_or_404

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    # 🔹 Getter para `language`
    @action(detail=True, methods=['get'])
    def get_language(self, request, pk=None):
        pet = self.get_object()
        return Response({"language": pet.language})

    # 🔹 Getter para `hunger`
    @action(detail=True, methods=['get'])
    def get_hunger(self, request, pk=None):
        pet = self.get_object()
        return Response({"hunger": pet.hunger})

    # 🔹 Getter para `is_dead`
    @action(detail=True, methods=['get'])
    def get_is_dead(self, request, pk=None):
        pet = self.get_object()
        return Response({"isDead": pet.isDead})

    # 🔹 Setter para `hunger`
    @action(detail=True, methods=['put'])  # Usa 'post' o 'patch' para modificar valores
    def set_hunger(self, request, pk=None):
        pet = self.get_object()
        hunger_value = request.data.get("hunger")

        if hunger_value is not None:
            try:
                if int(hunger_value) < 0:
                    return Response({"error": "Hunger value cannot be negative"}, status=status.HTTP_400_BAD_REQUEST)
                
                if pet.hunger == 100:
                    return Response({"error": "Pet is already full"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    pet.hunger += int(hunger_value)
                    pet.save()
                    return Response({"message": "Hunger updated successfully", "hunger": pet.hunger}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "Invalid hunger value"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Missing hunger value"}, status=status.HTTP_400_BAD_REQUEST)

    # 🔹 Setter para `is_dead`
    @action(detail=True, methods=['put'])
    def set_is_dead(self, request, pk=None):
        pet = self.get_object()
        is_dead_value = request.data.get("isDead")

        if is_dead_value is not None:
            pet.isDead = bool(is_dead_value)
            pet.save()
            return Response({"message": "isDead updated successfully", "isDead": pet.isDead}, status=status.HTTP_200_OK)

        return Response({"error": "Missing isDead value"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def get_accesories(self, request, pk=None):
        pet = self.get_object()
        accesories = pet.accesories.values("id", "image_path", "type")
        return Response({"accesories": list(accesories)})

    @action(detail=True, methods=['put'])
    def set_accesories(self, request, pk=None):
        print("Received request:", json.loads(request.body))
        pet = self.get_object()
        accesories_id = request.data.get("accesories")

        if accesories_id is not None:
            try:
                if accesories_id == "0" or accesories_id == 0:
                    pet.accesories.clear()
                    return Response({"message": "All accesories removed"}, status=status.HTTP_200_OK)

                accesories_id = int(accesories_id)

                clothes = get_object_or_404(Clothes, id=accesories_id)

                current_accesories = pet.accesories.all()

                existing_accesory = next((a for a in current_accesories if a.type == clothes.type), None)

                if existing_accesory:
                    pet.accesories.remove(existing_accesory)

                pet.accesories.add(clothes)

                return Response({
                    "message": "Accessory updated successfully",
                    "accesories": list(pet.accesories.values("id", "image_path", "type"))
                }, status=status.HTTP_200_OK)

            except ValueError:
                return Response({"error": "Invalid accesories value"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "Missing accesories value"}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'])
    def get_pet_by_player_and_language(self, request):
        """
        Obtiene una mascota por player_id y language.
        """
        player_id = request.query_params.get('player_id')
        language = request.query_params.get('language')

        if not player_id or not language:
            return Response({"error": "Se requieren player_id y language"}, status=status.HTTP_400_BAD_REQUEST)

        pet = Pet.objects.filter(player_id=player_id, language=language).first()

        if not pet:
            return Response({"error": "No se encontró una mascota con esos parámetros"}, status=status.HTTP_404_NOT_FOUND)

        return Response(PetSerializer(pet).data, status=status.HTTP_200_OK)