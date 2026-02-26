from django.contrib import admin
from .models import Cliente, RegistroAcesso

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone', 'data_cadastro', 'ativo')
    list_filter = ('nome', 'telefone', 'data_cadastro','setor', 'ativo')
    search_fields = ('nome', 'telefone', 'data_cadastro','setor', 'ativo' )
    ordering = ('nome', 'telefone', 'data_cadastro','setor', 'ativo')


@admin.register(RegistroAcesso)
class RegistroAcessoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_entrada', 'status_leitura')
    list_filter = ('cliente', 'data_entrada', 'status_leitura')
    search_fields = ('cliente', 'data_entrada', 'status_leitura')
    ordering = ('cliente', 'data_entrada', 'status_leitura')

