from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('api/user/', include('user.urls')),
    path('api/', include('food.urls')),
    path('api/', include('question.urls')),
    path('api/', include('clothes.urls')),
    path('api/', include('pet.urls')),
    path('api/', include('questionnarie.urls')),
]
