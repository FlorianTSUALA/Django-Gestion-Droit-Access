from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from access_control.models import Gestionnaire, Compte
from access_control.forms import GestionnaireForm, CompteCreationForm
import hashlib, binascii
from django.contrib.auth import (authenticate, login, logout, get_user_model, REDIRECT_FIELD_NAME)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, Permission
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings


# Liste de group
def liste_group(request):
    group = Group.objects.all()
    return render(request,'auth/liste_group.html',{'group':group})

# Add Group

def ajouter_group(request):
    if request.method == "POST":
        name = request.POST.get('name')
        perm = Group(
            name =  name
        )
        perm.save()
    else:
        return render(request,'permissions.html')
    return render(request,'permissions.html')

def permission(request):
    return render(request,'permission.html')

def delete_group(request,pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return 