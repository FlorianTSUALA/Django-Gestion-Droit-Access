from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _



from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import select2.fields
import select2.models

from .managers import CompteManager

# Create your models here.

class Compte(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=70, unique=True)
    telephone = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=250, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','telephone']

    objects = CompteManager()

    def __str__(self):
        return self.username


class Gestionnaire(models.Model):
    # compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    compte = select2.fields.ForeignKey(Compte,overlay="Choisir un compte...", on_delete=models.CASCADE)
    apropros = models.TextField(max_length=500, blank=True)
    residence = models.CharField(max_length=30, blank=True)
    date_naissance = models.DateField(null=True, blank=True)

class Developpeur(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    apropros = models.TextField(max_length=500, blank=True)
    residence = models.CharField(max_length=30, blank=True)
    date_naissance = models.DateField(null=True, blank=True)

class Profile(models.Model):
    gestionnaire = models.OneToOneField(Gestionnaire, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, blank=True)