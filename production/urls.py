from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductionViewSet, ProductionDeleteByDateViewSet

# Initialisation du routeur
router = DefaultRouter()
router.register(r'productions', ProductionViewSet, basename='productions')
router.register(r'productions-delete-by-date', ProductionDeleteByDateViewSet, basename='productions-delete-by-date')

# Inclusion des URLs générées par le routeur
urlpatterns = [
    path('', include(router.urls)),  # Inclure les URLs du routeur dans le projet
]
