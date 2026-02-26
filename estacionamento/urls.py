from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')), 
    path('', RedirectView.as_view(url='/cadastrar_cliente/', permanent=True)), 
    path('', include('cadastro.urls')), 
]