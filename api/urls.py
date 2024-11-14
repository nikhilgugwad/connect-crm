from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CustomerViewSet, SalesOpportunityViewSet, InteractionViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'opportunities', SalesOpportunityViewSet)
router.register(r'interactions', InteractionViewSet)

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
