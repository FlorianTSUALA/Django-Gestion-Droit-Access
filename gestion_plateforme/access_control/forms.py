from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Compte,Gestionnaire


class CompteCreationForm(UserCreationForm):

    class Meta:
        model = Compte
        fields = ('username', 'telephone', 'email', 'name')


class CompteChangeForm(UserChangeForm):

    class Meta:
        model = Compte
        fields = ('username', 'telephone', 'email', 'name')



class GestionnaireForm(forms.ModelForm):
    class Meta:
        model = Gestionnaire
        fields = (
            'compte',
            'apropros',
            'residence',
            'date_naissance',
        )