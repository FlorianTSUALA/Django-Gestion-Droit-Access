from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from access_control.models import Gestionnaire, Compte,Permission
from access_control.forms import GestionnaireForm
from access_control.models import Gestionnaire, Compte
from access_control.forms import GestionnaireForm, CompteCreationForm
import hashlib, binascii
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import User, Permission
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse


# # Create your views here.
# class IndexView(TemplateView):
#     template_name = 'index.html'
    
# class Login(LoginView):
#     template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = CompteCreationForm
    template_name = 'auth/auth_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

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
           dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd1), b'salt', 10000)
           password = binascii.hexlify(dk)
           print(password)
           compte= Compte(
                email = email,
                name = nom,
                username = username,
                telephone = telephone,
                password = password
                )
           compte.save()
           return redirect('login')

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'auth/auth_register.html')
        
    return render(request,'auth/auth_register.html')


def check_username(request):
    username = request.POST.get('username', None)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")
   

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
        password = binascii.hexlify(dk)
        print(utilisateur.password)
        print(password.decode("utf-8"))
        if str(password)== str(utilisateur.password):
            return redirect('gestionnaire')
        else:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
    else:
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