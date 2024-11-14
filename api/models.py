from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('sales', 'Salesperson'),
        ('customer', 'Customer'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class SalesOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stage = models.CharField(max_length=50)  # e.g., 'Lead', 'Negotiation', 'Closed'
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='opportunities')

    def __str__(self):
        return self.title

class Interaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)  # e.g., 'Call', 'Meeting', 'Email'
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    next_action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.interaction_type} with {self.customer.name} on {self.date}"

