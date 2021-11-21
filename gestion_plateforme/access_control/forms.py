from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Compte,Gestionnaire
import datetime
from django.contrib.admin import widgets

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
        # date_naissance = forms.DateField(initial=datetime.date.today)
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
