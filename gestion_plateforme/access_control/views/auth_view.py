from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from access_control.models import Gestionnaire, Compte
from access_control.forms import GestionnaireForm
import hashlib, binascii


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

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'auth/auth_register.html')
    return render(request,'auth/auth_register.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        utilisateur = Compte.objects.get(username=username)
        dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd), b'salt', 10000)
        passwo = binascii.hexlify(dk)
        print(utilisateur.password)
        print(passwo.decode("utf-8"))
        if str(passwo)== str(utilisateur.password):
            print('bravo jaures')
        # if user is not None:
        #     login(request,user)
        #     print(user.is_superuser)
        #     return redirect('home')
        else:
            # messages.error(request, "erreur t'authentification ")
            print('pas de permission')
            # return render(request, 'users/login.html',{'form':form})
    else:
        pass
        return render(request, 'auth/auth_login.html')


 