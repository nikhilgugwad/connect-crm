from rest_framework import viewsets
from .models import CustomUser, Customer, SalesOpportunity, Interaction
from .serializers import CustomUserSerializer, CustomerSerializer, SalesOpportunitySerializer, InteractionSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SalesOpportunityViewSet(viewsets.ModelViewSet):
    queryset = SalesOpportunity.objects.all()
    serializer_class = SalesOpportunitySerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
