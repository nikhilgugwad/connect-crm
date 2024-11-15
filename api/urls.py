from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CustomerViewSet, SalesOpportunityViewSet, InteractionViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'interactions', InteractionViewSet)  # Handle interaction data
router.register(r'users', CustomUserViewSet)  # Handle user data
router.register(r'customers', CustomerViewSet)  # Handle customer data
router.register(r'opportunities', SalesOpportunityViewSet)  # Handle sales opportunities

# API URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include router for all registered viewsets
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
]
