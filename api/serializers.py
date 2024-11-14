from rest_framework import serializers
from .models import CustomUser, Customer, SalesOpportunity, Interaction

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Or specify fields as needed

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # Or specify fields as needed

class SalesOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOpportunity
        fields = '__all__'  # Or specify fields as needed

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'  # Or specify fields as needed
