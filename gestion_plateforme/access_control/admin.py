from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CompteCreationForm, CompteChangeForm
from .models import Compte


class CompteAdmin(UserAdmin):
    add_form = CompteCreationForm
    form = CompteChangeForm
    model = Compte
    list_display = ('username', 'telephone', 'email', 'name', 'is_staff', 'is_active',)
    list_filter = ('username', 'telephone', 'email', 'name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Compte, CompteAdmin)