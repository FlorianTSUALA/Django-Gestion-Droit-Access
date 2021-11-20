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

from reservation.models import Compagnie


class GestionnaireForm(forms.ModelForm):
    class Meta:
        model = Gestionnaire
        fields = (
            'compte',
            'apropros',
            'residence',
            'date_naissance',
        )