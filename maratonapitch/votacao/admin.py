from django.contrib import admin
from .models import Startup, Voto, Comentario

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_atuacao', 'is_votacao_aberta', 'total_votos')
    list_filter = ('is_votacao_aberta',)
    search_fields = ('nome', 'area_atuacao')

@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'startup', 'criado_em')
    list_filter = ('startup',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'startup', 'criado_em')
    list_filter = ('startup',)
