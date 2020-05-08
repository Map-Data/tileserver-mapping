from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import timedelta
from django.utils import timezone
from secrets import token_urlsafe


def expiry_default():
    return timezone.now() + timedelta(3, 0, 0, 0, 0, 0, 0)


def token_default():
    return token_urlsafe(16)


class ServiceAccount(models.Model):
    description = models.CharField(max_length=120, default='', blank=True)
    expiry = models.DateTimeField(default=expiry_default)
    token = models.CharField(max_length=32, default=token_default, editable=False)

    @property
    def is_expired(self):
        return self.expiry < timezone.now()

    def renew(self):
        self.expiry = expiry_default()

    def __str__(self):
        return f'{self.__class__.__name__} ({self.description}) {self.token}'
