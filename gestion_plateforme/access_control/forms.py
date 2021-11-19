from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Compte


class CompteCreationForm(UserCreationForm):

    class Meta:
        model = Compte
        fields = ('username', 'telephone', 'email', 'name')


class CompteChangeForm(UserChangeForm):

    class Meta:
        model = Compte
        fields = ('username', 'telephone', 'email', 'name')