from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    organization_name = models.CharField(
        _('organization name'),
        max_length=255,
        blank=True,
        null=True,
        help_text='Наименование организации'
    )

    organization_inn = models.CharField(
        _('organization INN'),
        max_length=20,
        blank=True,
        null=True,
        help_text='ИНН организации'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
