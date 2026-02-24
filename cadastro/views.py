from django.shortcuts import render, get_object_or_404
from .models import Cliente, RegistroAcesso
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ClienteForm
import qrcode
import io
import base64
from django.urls import reverse
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm


def cadastrar_cliente(request):
    contexto = {}
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        contexto['form'] = form
        
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente {cliente.nome} cadastrado com sucesso!')
            
            url_caminho = reverse('validar_acesso', args=[cliente.codigo_acesso])
            url_completa = request.build_absolute_uri(url_caminho)
            
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(url_completa)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            img_base64 = base64.b64encode(buffer.getvalue()).decode()
            
            contexto['qr_code'] = f"data:image/png;base64,{img_base64}"
            contexto['cliente'] = cliente
            contexto['placa_veiculo'] = cliente.placa_veiculo
            contexto['form'] = ClienteForm() # Reseta o form para um novo cadastro
            
            return render(request, 'cadastro/cadastrar_cliente.html', contexto)
        else:
            # SE NÃO SALVAR, VAI MOSTRAR O MOTIVO EXATO AQUI NO TERMINAL:
            print("==== ERROS NO FORMULÁRIO ====")
            print(form.errors)
            print("=============================")
            
    else:
        contexto['form'] = ClienteForm()
        
    return render(request, 'cadastro/cadastrar_cliente.html', contexto)


def validar_acesso(request, codigo_acesso):
    cliente = get_object_or_404(Cliente, codigo_acesso=codigo_acesso)
    
    if cliente.ativo:
        RegistroAcesso.objects.create(cliente=cliente, status_leitura='Entrada')
        contexto = {
            'status': 'Entrada',
            'cor': 'success',
            'cliente': cliente
        }
    else:
        contexto = {
            'status': 'Entrada NEGADA',
            'cor': 'danger',
            'cliente': cliente,
            'Mensagem': 'Cliente inativo - Favor procurar a CSG'
        }
    return render(request, 'cadastro/validar_acesso.html', contexto)


def gerar_pdf_qrcode(request, codigo_acesso):
    cliente = get_object_or_404(Cliente, codigo_acesso=codigo_acesso)
    
    # Gerar a URL para o QR Code
    url_caminho = reverse('validar_acesso', args=[cliente.codigo_acesso])
    url_completa = request.build_absolute_uri(url_caminho)
    
    # Gerar a imagem do QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url_completa)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salvar a imagem num buffer
    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)
    
    # Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="qrcode_{cliente.placa_veiculo}.pdf"'
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4
    
    # Desenhar no PDF
    p.setFont("Helvetica-Bold", 16)
    p.drawCentredString(largura/2, altura - 3*cm, "Cartão de Acesso - SISAuto")
    
    p.setFont("Helvetica", 12)
    p.drawCentredString(largura/2, altura - 4*cm, f"Cliente: {cliente.nome} - Setor: {cliente.setor}")
    p.drawCentredString(largura/2, altura - 4.5*cm, f"Veículo: {cliente.modelo_veiculo} - Placa: {cliente.placa_veiculo}")
    
    # Inserir o QR Code
    from reportlab.lib.utils import ImageReader
    qr_img = ImageReader(img_buffer)
    p.drawImage(qr_img, (largura-10*cm)/2, altura - 15*cm, width=10*cm, height=10*cm)
    
    p.setFont("Helvetica-Oblique", 10)
    p.drawCentredString(largura/2, altura - 16*cm, "Apresente este QR Code na entrada do estacionamento.")
    
    p.showPage()
    p.save()
    
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response

