from datetime import timedelta
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.utils import timezone
from django.conf import settings

from . import models
from . import views

version = settings.REST_FRAMEWORK['DEFAULT_VERSION']


class AuthenticationTests(APITestCase):
    def setUp(self) -> None:
        self.service_account = models.ServiceAccount.objects.create()

    def test_no_token_no_auth(self):
        """
        Assert that no authentication is performed when no service-account token header is set
        """
        response = self.client.get(reverse('serviceaccount-list', kwargs={'version': version}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_auth(self):
        """
        Assert that authentication is performed when the service-account token header is set
        """
        response = self.client.get(reverse('serviceaccount-list', kwargs={'version': version}),
                                   HTTP_X_SERVICE_ACCOUNT=self.service_account.token)
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_expired_no_auth(self):
        """
        Assert that an expired token does not get authenticated
        """
        self.service_account.expiry = timezone.now() - timedelta(1)
        response = self.client.get(reverse('serviceaccount-list', kwargs={'version': version}),
                                   HTTP_X_SERVICE_ACCOUNT=self.service_account.token)


class AuthorizationTests(APITestCase):
    def setUp(self) -> None:
        self.service_account = models.ServiceAccount.objects.create()
        self.client.credentials(HTTP_X_SERVICE_ACCOUNT=self.service_account.token)

    def test_read_self(self):
        """
        Assert  that the authenticated client has read access to its own service account
        """
        response = self.client.get(reverse('serviceaccount-detail',
                                           kwargs={'version': version, 'pk': self.service_account.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_other(self):
        """
        Assert that other service-accounts cannot be read
        """
        other = models.ServiceAccount.objects.create()
        response = self.client.get(reverse('serviceaccount-detail',
                                           kwargs={'version': version, 'pk': other.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create(self):
        """
        Assert that everyone can create new service-accounts
        """
        self.client.credentials()
        response = self.client.post(reverse('serviceaccount-list', kwargs={'version': version}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
