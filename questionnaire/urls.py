from django.urls import path, include
from .views import QuestionnaireViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questionnaire', QuestionnaireViewSet, basename='questionnaire')

urlpatterns = router.urls