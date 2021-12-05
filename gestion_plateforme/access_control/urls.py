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
from access_control.views import (
    login, 
    logout_block, 
    register,
    check_username,
    RegisterView,
)

from access_control.views import (
    liste_permission,
)


from access_control.views import (
    gestionnaire_create, 
    gestionnaire_update, 
    gestionnaire_delete, 
    gestionnaire,
     
    profile_create, 
    profile_update, 
    profile_delete, 
    profile,

)


urlpatterns = [
    #account access

    path('gestionnaire/',  gestionnaire, name='gestionnaire'),
    path('gestionnaire/gestionnaire_create/',  gestionnaire_create, name='gestionnaire_create'),
    path('gestionnaire/<int:pk>/update/',  gestionnaire_update, name='gestionnaire_update'),
    path('gestionnaire/<int:pk>/delete/',  gestionnaire_delete, name='gestionnaire_delete'),
    

    path('profile/',  profile, name='profile'),
    path('profile/profile_create/',  profile_create, name='profile_create'),
    path('profile/<int:pk>/update/',  profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/',  profile_delete, name='profile_delete'),
    
    path('register/',  RegisterView.as_view(), name="register"),
    # path('register/',  register, name='register'),
    path('login/',  login, name='login'),
    path('logout/',  logout_block, name='logout'),
    
    path('liste_permission/',  liste_permission, name='liste_permission'),



    # # # #     Gestionnaire
    path('',  views.accueil, name='accueil'),
    path('gestionnaire/',  views.gestionnaire, name='gestionnaire'),
    path('gestionnaire/create/',  views.gestionnaire_create, name='gestionnaire_create'),
    path('gestionnaire/<int:pk>/update/',  views.gestionnaire_update, name='gestionnaire_update'),
    path('gestionnaire/<int:pk>/delete/',  views.gestionnaire_delete, name='gestionnaire_delete'),
    path('register/',  views.register, name='register'),
    path('login/',  views.login, name='login'),
    path('logout/',  views.logout_block, name='logout'),
    path('liste_permission/',  views.liste_permission, name='liste_permission'),
    path('permission/',  views.permission, name='permission'),
    path('ajourter_permission/',  views.ajourter_permission, name='ajourter_permission'),
    path('liste_group/',  views.liste_group, name='liste_group'),

]


htmx_urlpatterns = [
    path('check_username/', check_username, name='check-username')
]

urlpatterns += htmx_urlpatterns