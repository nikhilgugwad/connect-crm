from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    
    In addition to the standard fields (username, email, password, etc.), this model adds:
    - 'role': Specifies the role of the user (Admin, Salesperson, Customer).
    - 'groups' and 'user_permissions' are overridden to support custom user roles and permissions.

    This model is used for managing users within the ConnectCRM system.
    """
    
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("sales", "Salesperson"),
        ("customer", "Customer"),
    )
    
    # Role field for different user types
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

    # Many-to-many relationships for user groups and permissions
    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_permissions"
    )

    def __str__(self):
        """
        String representation of the CustomUser object, returning the username.
        """
        return self.username

    class Meta:
        # Custom permissions for user actions
        permissions = (
            ("can_view_sales_opportunities", "Can view sales opportunities"),
            ("can_manage_customers", "Can manage customers"),
            ("can_create_interactions", "Can create interactions"),
        )


class Customer(models.Model):
    """
    Model representing a customer in the CRM system.
    
    This model stores basic information about customers including their:
    - name
    - email
    - phone
    - address
    
    It also establishes a relationship with the `CustomUser` model, linking each customer to a user.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String representation of the Customer object, returning the customer's name.
        """
        return self.name


class SalesOpportunity(models.Model):
    """
    Model representing a sales opportunity.
    
    This model tracks information about sales opportunities such as:
    - title
    - description
    - stage (e.g., 'Lead', 'Negotiation', 'Closed')
    - customer associated with the opportunity
    - the user assigned to the opportunity

    It is used for managing the sales pipeline.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    stage = models.CharField(max_length=50)  # e.g., 'Lead', 'Negotiation', 'Closed'
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="opportunities"
    )

    def __str__(self):
        """
        String representation of the SalesOpportunity object, returning the title.
        """
        return self.title


class Interaction(models.Model):
    """
    Model representing an interaction with a customer.

    This model captures the details of an interaction, including:
    - type of interaction (e.g., Call, Meeting, Email)
    - notes about the interaction
    - date of the interaction
    - any next actions that need to be followed up on.

    This is useful for tracking communication with customers.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    interaction_type = models.CharField(
        max_length=50
    )  # e.g., 'Call', 'Meeting', 'Email'
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    next_action = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation of the Interaction object, returning a description of the interaction.
        """
        return f"{self.interaction_type} with {self.customer.name} on {self.date}"
