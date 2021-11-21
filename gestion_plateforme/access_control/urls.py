"""Compagnie_aerienne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from access_control import views
from access_control.views import gestionnaire,auth_view


urlpatterns = [
    #account access
    




    # # # #     Gestionnaire
    #path('',  views.accueil, name='accueil'),
    path('gestionnaire/',  views.gestionnaire, name='gestionnaire'),
    path('gestionnaire/create/',  views.gestionnaire_create, name='gestionnaire_create'),
    path('gestionnaire/<int:pk>/update/',  views.gestionnaire_update, name='gestionnaire_update'),
    path('gestionnaire/<int:pk>/delete/',  views.gestionnaire_delete, name='gestionnaire_delete'),
    path('register/',  views.register, name='register'),
    path('login/',  views.login, name='login'),

]
