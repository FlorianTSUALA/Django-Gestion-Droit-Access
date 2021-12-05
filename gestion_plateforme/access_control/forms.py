from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Compte, Gestionnaire, Profile
import datetime
from django.contrib.admin import widgets
from django.forms.widgets import NumberInput

class CompteCreationForm(UserCreationForm):
    
    class Meta:
        model = Compte
        fields = ['username', 'telephone', 'email', 'name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CompteCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Login'

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

    def __init__(self, *args, **kwargs):
        super(GestionnaireForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )

            if field == 'compte':
                pass

        self.fields['date_naissance'].widget.input_type = 'date'

        self.fields['compte'].widget.attrs['class'] = 'form-control select2'
        self.fields['compte'].widget.attrs['style'] = 'width: 100%;'
        self.fields['compte'].initial = 'choisir une valeur'

        self.fields['apropros'].widget.attrs.update({'rows': '2'})

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        # permissions = forms.ChoiceField( choices = Permission.objects.all(), overlay="Choisir une permission..." )

        fields = (
            'name',
            'permissions',
        )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            new_data = { "class": 'form-control', }
            self.fields[str(field)].widget.attrs.update( new_data )

        self.fields['permissions'].widget.attrs['class'] = 'form-control select2'
        self.fields['permissions'].widget.attrs['style'] = 'width: 100%;'
        self.fields['permissions'].widget.attrs['multiple'] = 'multiple'

