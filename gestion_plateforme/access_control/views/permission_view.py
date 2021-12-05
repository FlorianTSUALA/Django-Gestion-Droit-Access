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
from django.contrib.auth.models import User, Permission
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings

def permission(request):
    permissions = Permission.objects.all()
    for p in permissions:
        print(p.name +' '+ p.codename)
    return render(request, 'partials/permission/list.html',{permissions: permissions})
