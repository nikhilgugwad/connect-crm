from rest_framework import serializers
from .models import CustomUser, Customer, SalesOpportunity, Interaction

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model, representing user data, 
    including roles, permissions, and related data.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')  # Explicitly define necessary fields


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model, representing customer information.
    """
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'phone', 'address', 'user')  # Explicitly define necessary fields


class SalesOpportunitySerializer(serializers.ModelSerializer):
    """
    Serializer for the SalesOpportunity model, representing sales opportunities linked to customers.
    """
    class Meta:
        model = SalesOpportunity
        fields = ('id', 'title', 'description', 'stage', 'customer', 'assigned_to')  # Explicitly define necessary fields


class InteractionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Interaction model, representing customer interactions in the CRM.
    """
    class Meta:
        model = Interaction
        fields = ('id', 'customer', 'interaction_type', 'notes', 'date', 'next_action')  # Explicitly define necessary fields
