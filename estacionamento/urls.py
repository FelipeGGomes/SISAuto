from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. Adicione esta linha: Ela pega a raiz do site ('') e joga para o cadastro
    path('', RedirectView.as_view(url='/cadastrar_cliente/', permanent=True)), 
    
    # 3. Mantém as urls do seu app funcionando normalmente
    path('', include('cadastro.urls')), 
]