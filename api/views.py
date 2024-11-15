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
    """
    Viewset for handling CustomUser data.
    Only accessible to Admin users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]  # Only admins can view user data

class CustomerViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling Customer data.
    Accessible to Admins and Salespersons.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsSalesperson | IsAdmin]  # Salesperson and Admins can manage customers

class SalesOpportunityViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Sales Opportunities.
    Accessible to Admins and Salespersons.
    """
    queryset = SalesOpportunity.objects.all()
    serializer_class = SalesOpportunitySerializer
    permission_classes = [IsSalesperson | IsAdmin]  # Salesperson and Admins can manage opportunities

class InteractionViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Interactions with customers.
    Accessible to Admins, Salespersons, and Customers.
    """
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsSalesperson | IsAdmin | IsCustomer]

    def get_queryset(self):
        """
        Custom queryset based on the user's role:
        - Customers can only see their interactions.
        - Admins and Salespersons can see all interactions.
        """
        user = self.request.user

        if user.role == "customer":
            # Customers can only see their own interactions
            return Interaction.objects.filter(customer__user=user)
        elif user.role in ["admin", "sales"]:
            # Admins and Salespeople can see all interactions
            return Interaction.objects.all()
        return Interaction.objects.none()  # Return empty if no valid role
