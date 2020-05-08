from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from django.contrib.auth.models import AnonymousUser
from . import models


class ServiceAccountTokenAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        if 'HTTP_X_SERVICE_ACCOUNT' in request.META.keys():
            try:
                sa = models.ServiceAccount.objects.get(token__exact=request.META.get('HTTP_X_SERVICE_ACCOUNT'))
                if sa.is_expired:
                    raise AuthenticationFailed('ServiceAccount expired')
                return AnonymousUser(), sa
            except models.ServiceAccount.DoesNotExist:
                raise AuthenticationFailed('ServiceAccount does not exist')
