from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser, Customer, SalesOpportunity, Interaction
from .serializers import (
    CustomUserSerializer,
    CustomerSerializer,
    SalesOpportunitySerializer,
    InteractionSerializer,
)
from .permissions import IsAdmin, IsSalesperson, IsCustomer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]  # Only admins can view user data

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [
        IsSalesperson | IsAdmin
    ]  # Salesperson and Admins can manage customers

class SalesOpportunityViewSet(viewsets.ModelViewSet):
    queryset = SalesOpportunity.objects.all()
    serializer_class = SalesOpportunitySerializer
    permission_classes = [
        IsSalesperson | IsAdmin
    ]  # Salesperson and Admins can manage opportunities

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()  # Default queryset
    serializer_class = InteractionSerializer
    permission_classes = [IsSalesperson | IsAdmin | IsCustomer]

    def get_queryset(self):
        user = self.request.user

        # Customers should only see their interactions
        if user.role == "customer":
            return Interaction.objects.filter(customer__user=user)
        # Admins and Salespeople can see all interactions
        elif user.role in ["admin", "sales"]:
            return Interaction.objects.all()
        # If no valid role, return an empty queryset
        return Interaction.objects.none()
