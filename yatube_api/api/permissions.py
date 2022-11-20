from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'author'):
            return obj.author == request.user or request.method\
                   in permissions.SAFE_METHODS
        else:
            return request.method in permissions.SAFE_METHODS
