from django.urls import path
from .views import PendingRegistrationView, ConfirmRegistration

urlpatterns = [
    path('registration', PendingRegistrationView.as_view(), name='pending_registration'),
    path('confirm-registration', ConfirmRegistration.as_view(), name='confirm_registration'),
]
