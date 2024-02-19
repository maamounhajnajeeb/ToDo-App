from rest_framework.request import Request
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request: Request, view, obj):
        return True if request.user == obj.due_date.user else False
