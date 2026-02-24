from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        
        fields = ['nome', 'cpf', 'telefone', 'setor', 'placa_veiculo', 'modelo_veiculo'] 
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'setor': forms.Select(attrs={'class': 'form-select'}), # Note que mudei para form-select aqui para o Bootstrap
            'placa_veiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC-1234'}),
            'modelo_veiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Honda Civic'}),
        }
        error_messages = {
            'placa_veiculo': {
                'unique': "Já existe um cliente cadastrado com esta placa.",
            },
        }