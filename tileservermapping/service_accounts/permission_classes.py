from rest_framework.permissions import BasePermission


class RequestAuthToItself(BasePermission):
    """
    A permission class which grants the `request.auth` object access to itself
    """

    def has_object_permission(self, request, view, obj):
        return request.auth is not None and request.auth == obj
