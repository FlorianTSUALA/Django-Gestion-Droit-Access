from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
# Create your views here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CompteManager

# Create your models here.

class Compte(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=50, unique=True)
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

class Profile(models.Model):
    libelle = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, blank=True)

class Gestionnaire(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    apropros = models.TextField(max_length=500, blank=True)
    residence = models.CharField(max_length=30, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

class Developpeur(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    apropros = models.TextField(max_length=500, blank=True)
    residence = models.CharField(max_length=30, blank=True)
    date_naissance = models.DateField(null=True, blank=True)


class Permission(models.Model):
    libelle = models.CharField(max_length=30, blank=True)
    profile = models.ManyToManyField(Profile)
class Profile(Group):

    class Meta:
        proxy = True
    
    def __str__(self):
        return self.name

class Permission(Permission):

    class Meta:
        proxy = True
    
    def __str__(self):
        name = self.name.replace('Can', 'Peut')
        print("name")
        print(name)
        return name
