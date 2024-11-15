from django.contrib import admin
from .models import CustomUser, Customer, SalesOpportunity, Interaction

# Register the CustomUser model with the Django admin interface.
# This allows managing users directly from the admin panel.
admin.site.register(CustomUser)

# Register the SalesOpportunity model to enable managing sales opportunities via the admin panel.
admin.site.register(SalesOpportunity)

# Register the Interaction model to facilitate managing customer interactions from the admin interface.
admin.site.register(Interaction)

# Custom display options for the Customer model in the admin interface.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customize the admin panel for the Customer model.

    This class specifies how the Customer model will be displayed in the Django admin interface.
    """
    
    # Fields to display in the list view of the Customer model.
    list_display = ('name', 'email', 'phone')

    # Fields to be used for search functionality in the admin panel.
    search_fields = ('name', 'email')
