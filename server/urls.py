from django.urls import path, re_path, include
#from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Ballingo API",
      default_version='v1',
      description="API developed for the Ballingo project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ballingo@team.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('api/user/', include('user.urls')),
   path('api/', include('food.urls')),
   path('api/', include('question.urls')),
   path('api/', include('clothes.urls')),
   path('api/', include('pet.urls')),
   path('api/', include('questionnaire.urls')),
   path('api/', include('foodItem.urls')),
   path('api/', include('foodList.urls')),
   path('api/', include('wardrobe.urls')),
   path('api/', include('trade.urls')),
   path('api/', include('language.urls')),
   path('api/', include('shopItem.urls')),
   path('api/', include('realPack.urls')),
   path('api/', include('gamePack.urls')),
   path('api/', include('playerProgress.urls')),
   path('api/', include('inventory.urls')),
   path('api/', include('player.urls')),

   path('docs/', schema_view.with_ui('swagger', cache_timeout=0)), # <-- Documenation
]
