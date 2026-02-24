from django.urls import path
from . import views



urlpatterns = [
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('validar_acesso/<str:codigo_acesso>/', views.validar_acesso, name='validar_acesso'),
    path('gerar_pdf_qrcode/<str:codigo_acesso>/', views.gerar_pdf_qrcode, name='gerar_pdf_qrcode'),
]