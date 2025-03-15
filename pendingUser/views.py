from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import PendingRegistration
from .serializers import PendingRegistrationSerializer
from user.serializers import BallingoUserSerializer
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from utils.utils import generate_recovery_code
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

def confirmation_email(email, code, user):
        subject = '🔍 Email Address Confirmation'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        text_message = (
            f"Hello {user.username},\n\n"
            "We've sent you this email to validate your email address. Use the following code for validation:\n\n"
            f"🔢 Your confirmation code: {code}\n\n"
            "Best regards,\nThe Ballingo Team"
        )

        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 500px; margin: auto; padding: 20px; border-radius: 10px; background: #f9f9f9; text-align: center;">
                    <h2 style="color: #007bff;">🔍 Email Address Confirmation</h2>
                    <p>Hello <strong>{user.username}</strong>,</p>
                    <p>We've sent you this email to validate your email address. Use the following code for validation:</p>
                    <p style="font-size: 24px; font-weight: bold; background: #007bff; color: white; padding: 10px; border-radius: 5px; display: inline-block;">
                        {code}
                    </p>
                    <br>
                    <p style="color: #777;">Best regards,<br><strong>The Ballingo Team</strong></p>
                </div>
            </body>
        </html>
        """

        email = EmailMultiAlternatives(subject, text_message, from_email, recipient_list)
        email.attach_alternative(html_message, "text/html")
        email.send(fail_silently=False)

class PendingRegistrationView(generics.CreateAPIView):
    queryset = PendingRegistration.objects.all()
    serializer_class = PendingRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        confirmation_code = generate_recovery_code()
        data['confirmation_code'] = confirmation_code

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            pending_user = serializer.save()
            confirmation_email(pending_user.email, confirmation_code, pending_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmRegistration(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data)
        email = request.data.get('email')
        code = request.data.get('confirmation_code')
    
        if not email or not code:
            return Response({'error': 'Email and confirmation code are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        pending_user = get_object_or_404(PendingRegistration, email=email)

        if pending_user.confirmation_code == code:
            user_data = {
                'email': pending_user.email,
                'username': pending_user.username,
                'password': pending_user.password,
            }

            serializer = BallingoUserSerializer(data=user_data)
            if serializer.is_valid():
                user = serializer.save()
                token, created = Token.objects.get_or_create(user=user)
                pending_user.delete()
                return Response({
                    'message': 'User created successfully',
                    'token': token.key,
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
