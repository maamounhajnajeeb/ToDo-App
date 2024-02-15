from rest_framework import permissions, request


class NotAuthenticated(permissions.BasePermission):
    def has_permission(self, request: request.Request, view):
        if request.user.is_authenticated:
            return False
        return True
    
    def has_object_permission(self, request: request.Request, view, obj):
        if request.user.is_authenticated:
            return False
        return True
