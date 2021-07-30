from rest_framework.permissions import BasePermission


class AnonymousPermission(BasePermission):
    """
    check permission
    """
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return True