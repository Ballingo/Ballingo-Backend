from django.urls import path, include
from .views import QuestionnarieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questionnarie', QuestionnarieViewSet, basename='questionnarie')

urlpatterns = router.urls