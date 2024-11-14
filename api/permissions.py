from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to users with the 'admin' role.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsSalesperson(BasePermission):
    """
    Allows access only to users with the 'sales' role.
    """
    def has_permission(self, request, view):
        return request.user.role == 'sales'

class IsCustomer(BasePermission):
    """
    Allows access only to users with the 'customer' role.
    """
    def has_permission(self, request, view):
        return request.user.role == 'customer'
