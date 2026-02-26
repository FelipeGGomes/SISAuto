from django.contrib import admin
from django.utils.html import mark_safe 
from django.urls import reverse
from .models import Cliente, RegistroAcesso

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','setor','telefone', 'data_cadastro', 'ativo')
    list_filter = ('nome', 'telefone', 'data_cadastro','setor', 'ativo')
    search_fields = ('nome', 'telefone', 'data_cadastro','setor', 'ativo' )
    ordering = ('nome', 'telefone', 'data_cadastro','setor', 'ativo')
    
    readonly_fields = ['visualizar_qrcode']
    
    def visualizar_qrcode(self, obj):
        if obj and obj.pk and obj.codigo_acesso:
            # AGORA APONTA PARA A VIEW DO PDF!
            url_pdf = reverse('gerar_pdf_qrcode', args=[str(obj.codigo_acesso)])
            
            return mark_safe(f'''
                <a href="{url_pdf}" target="_blank" style="background-color: #1b2b3a; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: bold; font-size: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-earmark-pdf" viewBox="0 0 16 16" style="vertical-align: text-bottom; margin-right: 5px;">
                        <path d="M14 14V4.5L9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2zM9.5 3A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5v2z"/>
                        <path d="M4.603 14.087a.81.81 0 0 1-.438-.42c-.195-.388-.13-.776.08-1.102.198-.307.526-.568.897-.787a7.68 7.68 0 0 1 1.482-.645 19.697 19.697 0 0 0 1.062-2.227 7.269 7.269 0 0 1-.43-1.295c-.086-.4-.119-.796-.046-1.136.075-.354.274-.672.65-.823.192-.077.4-.12.602-.077a.7.7 0 0 1 .477.365c.088.164.12.356.127.538.007.188-.012.396-.047.614-.084.51-.27 1.134-.52 1.794a10.954 10.954 0 0 0 .98 1.686 5.753 5.753 0 0 1 1.334.05c.364.066.734.195.96.465.12.144.193.32.2.518.007.192-.047.382-.138.563a1.04 1.04 0 0 1-.354.416.856.856 0 0 1-.51.138c-.331-.014-.654-.196-.933-.417a5.712 5.712 0 0 1-.911-.95 11.651 11.651 0 0 0-1.997.406 11.307 11.307 0 0 1-1.02 1.51c-.292.35-.609.656-.927.787a.793.793 0 0 1-.58.029zm1.379-1.901c-.166.076-.32.156-.459.238-.328.194-.541.383-.647.547-.094.145-.096.25-.04.361.01.022.02.036.026.044a.266.266 0 0 0 .023-.012c.152-.086.305-.23.446-.383.213-.23.411-.5.552-.795zm2.087-.41c.065-.01.13-.02.196-.03.218-.032.436-.062.65-.084l.012-.001a14.542 14.542 0 0 0-.58-1.027 11.97 11.97 0 0 0-.278 1.142zm1.488-1.55c-.14-.3-.284-.6-.43-.895a5.454 5.454 0 0 1-.039-.078c.08-.22.15-.443.21-.667.14-.52.22-1.04.22-1.528a2.59 2.59 0 0 0-.01-.318c-.01-.01-.01-.02-.01-.03-.004-.007-.007-.015-.01-.024-.01-.02-.02-.03-.02-.03-.02-.03-.05-.04-.08-.04-.03 0-.06.01-.08.03-.02.02-.04.05-.05.09-.01.04-.02.1-.02.17-.01.21.02.5.08.82.04.21.09.43.15.65zm2.41 1.07c.05-.06.1-.12.14-.17.06-.1.1-.2.12-.3.02-.1.02-.19-.01-.26-.03-.06-.08-.09-.12-.1-.04-.01-.09-.01-.15-.01-.16.02-.33.11-.5.25-.13.11-.25.25-.36.4.21.06.41.11.61.15.06.01.12.02.17.04z"/>
                    </svg>
                    Imprimir Cartão de Acesso (PDF)
                </a>
                <p style="margin-top: 8px; font-size: 12px; color: #888;">
                    Gera um documento formato A4 pronto para impressão.
                </p>
            ''')
        return "⚠️ Salve o cliente primeiro para gerar o PDF."
    
    visualizar_qrcode.short_description = "QR Code de Acesso"
    


@admin.register(RegistroAcesso)
class RegistroAcessoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_entrada', 'status_leitura')
    list_filter = ('cliente', 'data_entrada', 'status_leitura')
    search_fields = ('cliente', 'data_entrada', 'status_leitura')
    ordering = ('cliente', 'data_entrada', 'status_leitura')

