from django.shortcuts import render
from django.contrib.auth.models import User, Permission
from django.db.models import Q

# def permissions(request):
#     perm = Permission.objects.all() 
#     # users = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm)).distinct()
#     for p in perm:
#         print(p.name)
#     return render(request)

