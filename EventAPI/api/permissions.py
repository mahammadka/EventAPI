from rest_framework.permissions import BasePermission

# Custom permission to check if the user is an admin
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

# Custom permission to check if the user is a regular user
class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'