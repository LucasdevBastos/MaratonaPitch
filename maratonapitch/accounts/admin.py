from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações da Maratona', {'fields': ('tipo_publico',)}),
    )
    list_display = ('username', 'email', 'tipo_publico', 'is_staff', 'is_active')
