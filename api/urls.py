from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CustomerViewSet, SalesOpportunityViewSet, InteractionViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'interactions', InteractionViewSet)  # Register first for clarity
router.register(r'users', CustomUserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'opportunities', SalesOpportunityViewSet)

# Map the interactions endpoint directly to verify view accessibility
urlpatterns = [
    path('', include(router.urls)),  # Include router for all registered viewsets
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]



