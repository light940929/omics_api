from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Unauthenticated users can still read.
    Assumes the model instance has a `user` attribute.
    """
    def has_permission(self, request, view):
        """
        This is specifically to use PUT for bulk updates, where it appears DRF does not use `has_object_permission`
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, User):
            return obj == request.user
        else:
            return obj.user == request.user

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request.user, view)
