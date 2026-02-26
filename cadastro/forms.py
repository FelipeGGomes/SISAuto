from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        
        fields = ['nome', 'cpf', 'telefone', 'setor'] 
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'setor': forms.Select(attrs={'class': 'form-select'}),

        }
        error_messages = {
            'cpf': {
                'unique': "Já existe um cliente cadastrado com este CPF.",
            },
        }