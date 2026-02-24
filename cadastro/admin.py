from django.contrib import admin
from .models import Cliente, RegistroAcesso

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone', 'data_cadastro','placa_veiculo', 'ativo')
    list_filter = ('nome', 'telefone', 'data_cadastro','placa_veiculo', 'ativo')
    search_fields = ('nome', 'telefone', 'data_cadastro','placa_veiculo', 'ativo' )
    ordering = ('nome', 'telefone', 'data_cadastro','placa_veiculo', 'ativo')

admin.site.register(Cliente, ClienteAdmin)


class RegistroAcessoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_entrada', 'status_leitura')
    list_filter = ('cliente', 'data_entrada', 'status_leitura')
    search_fields = ('cliente', 'data_entrada', 'status_leitura')
    ordering = ('cliente', 'data_entrada', 'status_leitura')

admin.site.register(RegistroAcesso, RegistroAcessoAdmin)
