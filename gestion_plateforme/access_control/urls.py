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
from django.urls import path, include, re_path
from access_control.views import (
    permission_view,
    user_login, 
    user_logout, 
    register,
    check_username,
    RegisterView,
)

from access_control.views import (
    permission,
)


from access_control.views import (
    gestionnaire_create, 
    gestionnaire_update, 
    gestionnaire_delete, 
    gestionnaire,

    liste_group,
     
    profile_create, 
    profile_update, 
    profile_delete, 
    profile,

    ModelIndexView,
    home_model,    
    check_libelle,
    search_model,
    add_model,
    update_model,
    delete_model,

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
    
    # path('register/',  RegisterView.as_view(), name="register"),
    path('register/',  register, name='register'),
    path('login/',  user_login, name='login'),
    path('logout/',  user_logout, name='logout'),
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']

    path('liste_permission/',  liste_permission, name='liste_permission'),

    # # # #     Gestionnaire
    # path('',  accueil, name='accueil'),
    path('gestionnaire/',  gestionnaire, name='gestionnaire'),
    path('gestionnaire/create/',  gestionnaire_create, name='gestionnaire_create'),
    path('gestionnaire/<int:pk>/update/',  gestionnaire_update, name='gestionnaire_update'),
    path('gestionnaire/<int:pk>/delete/',  gestionnaire_delete, name='gestionnaire_delete'),
    path('register/',  register, name='register'),
    path('liste_permission/',  liste_permission, name='liste_permission'),

    path('permission/',  permission_view, name='permission'),
    path('ajourter_permission/',  ajourter_permission, name='ajourter_permission'),
    path('liste_group/',  liste_group, name='liste_group'),

]


htmx_urlpatterns = [
    path('check_username/', check_username, name='check-username'),

    path('model/home/',  ModelIndexView.as_view(), name='home-model'),
    path('model/search/',  search_model, name='search-model'),
    path('model/add/',  add_model, name='add-model'),
    path('model/check/libelle', check_libelle, name='check-model'),
    path('model/update/<int:pk>/',  update_model, name='update-model'),
    path('model/delete/<int:pk>/',  delete_model, name='delete-model'),

]

urlpatterns += htmx_urlpatterns