from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from access_control.models import Gestionnaire, Compte,Permission
from access_control.forms import GestionnaireForm
import hashlib, binascii
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User, Permission


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        pwd1 = request.POST.get('passw1')
        pwd2 = request.POST.get('passw2')
        if pwd1 !=pwd2:
            message = 'Les mots de passes ne sont pas identique'
            return render(request,'auth/auth_register.html',{'message':message})
        else:
        #    passwo = hashlib.sha224().hexdigest()
           dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd1), b'salt', 10000)
           passwo = binascii.hexlify(dk)
           print(passwo)
           compte= Compte(
                email = email,
                name = nom,
                username = username,
                telephone = telephone,
                password = passwo
                )
           compte.save()
           return redirect('login')

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'auth/auth_register.html')
    return render(request,'auth/auth_register.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            utilisateur = Compte.objects.get(username=username)
        except ObjectDoesNotExist:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
        dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd), b'salt', 10000)
        passwo = binascii.hexlify(dk)
        print(utilisateur.password)
        print(passwo.decode("utf-8"))
        if str(passwo)== str(utilisateur.password):
            return redirect('gestionnaire')
        else:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
    else:
        pass
        return render(request, 'auth/auth_login.html')

def logout_block(request):
    logout(request)
    return redirect('login')
# Liste de permissions 
def liste_permission(request):
    perm = Permission.objects.all()
    for p in perm:
        print(p.name +' '+ p.codename)
    return render(request,'auth/auth_register.html')

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

def ajourter_permission(request):
    if request.method == "POST":
        libele = request.POST.get('libele')
        perm = Permission(
            libelle =  libele
        )
        perm.save()
    else:
        return render(request,'permissions.html')
    return render(request,'permissions.html')

def delete_group(request,pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return 