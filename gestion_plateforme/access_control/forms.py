from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Compte,Gestionnaire
import datetime
from django.contrib.admin import widgets
from django.forms.widgets import NumberInput

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
        # compte = forms.ChoiceField(label='CompteA :', class ='form-control select2', required=True)
        # compte = forms.ChoiceField(label='CompteA :', class ='form-control select2', required=True)
        compte = forms.ChoiceField( widget=forms.Select(attrs={'class': 'form-control select2'}) )
        # date_naissance = forms.DateField(initial=datetime.date.today)
        # date_naissance = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
        fields = (
            'compte',
            'apropros',
            # 'residence',
            'date_naissance',
        )
        # widgets = {
        #     'date_naissance': forms.DateInput()
        # }


#   username=forms.CharField(widget=forms.TextInput(attrs={'onchange': 'this.form.submit();', 'class': 'editinput'}))

    def __init__(self, *args, **kwargs):
        super(GestionnaireForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                # "placeholder": f'Recipe {str(field)}',
                "class": 'form-control pro',
                # "hx-post": ".",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
            if field == 'compte':
                self.fields[str(field)].widget.attrs.update(
                {'class': 'form-control select2'}
                )
                print('Yess ')
                print(self.fields[str(field)].widget.attrs)
                print(self.fields['compte'].widget)
                print(self.fields['compte'])
                self.fields[str(field)].widget.attrs['class'] = 'form-control 5'
        # self.fields['date_naissance'].widget.attrs.update({'type': 'datetime-local'})
        self.fields['date_naissance'].widget.input_type = 'date'
        # self.fields['compte'].widget.class_name = 'form-control select2'
        # self.fields['date_naissance'].widget.attrs.update({'type': 'datetime-local'})
        # self.fields['date_naissance'].widget = widgets.AdminDateWidget()
        # subject = forms.CharField(label='subject', max_length=100 , widget=forms.TextInput(attrs={'class': "form-control"}))

        self.fields['compte'].widget.attrs.update(  {
                                                        # 'class': 'form-control select2', 
                                                        # 'style': 'width: 100%;', 
                                                        'label': 'Compte :'
                                                    }
                                                )
        self.fields['compte'].widget.attrs['class'] = 'form-control select2'
        # self.fields['compte'] = forms.ChoiceField( widget=forms.Select(attrs={'class': 'form-control select2'}) ) 
        # self.fields['compte'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['apropros'].widget.attrs.update({'rows': '2'})
        self.fields['compte'].initial = 'choisir une valeur'
