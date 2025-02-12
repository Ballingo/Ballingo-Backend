from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import BallingoUser
from .serializers import BallingoUserSerializer

class SignupView(generics.CreateAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Credenciales inválidas'}, status=400)