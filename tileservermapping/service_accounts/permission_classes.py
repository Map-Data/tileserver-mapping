from rest_framework.permissions import BasePermission

from . import models


class RequestAuthToItself(BasePermission):
    """
    A permission class which grants the `request.auth` object access to itself
    """

    def has_object_permission(self, request, view, obj):
        return request.auth is not None and request.auth == obj


class RequestAuthIsManagingThis(BasePermission):
    """
    Grants access to an object if the objects `managed_by` property is a foreign key that points to the
    `request.auth` object
    """
    def has_object_permission(self, request, view, obj):
        return hasattr(obj, 'managed_by') and obj.managed_by == request.auth


class IsServiceAccountAuthenticated(BasePermission):
    """
    Grants access when the request is authenticated by a service-account
    """
    def has_permission(self, request, view):
        return request.auth is not None and isinstance(request.auth, models.ServiceAccount)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

