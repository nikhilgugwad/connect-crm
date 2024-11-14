from django.contrib import admin
from .models import CustomUser, Customer, SalesOpportunity, Interaction

# Register CustomUser, SalesOpportunity, and Interaction
admin.site.register(CustomUser)
admin.site.register(SalesOpportunity)
admin.site.register(Interaction)

# Custom display options for the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
