from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to grant access only to users with the 'admin' role.
    """
    def has_permission(self, request, view):
        # Check if the authenticated user has the 'admin' role
        return request.user.role == 'admin'


class IsSalesperson(BasePermission):
    """
    Custom permission to grant access only to users with the 'sales' role.
    """
    def has_permission(self, request, view):
        # Check if the authenticated user has the 'sales' role
        return request.user.role == 'sales'


class IsCustomer(BasePermission):
    """
    Custom permission to grant access only to users with the 'customer' role.
    """
    def has_permission(self, request, view):
        # Check if the authenticated user has the 'customer' role
        return request.user.role == 'customer'
