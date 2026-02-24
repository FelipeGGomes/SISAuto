from django.db import models
import uuid
# Create your models here.

class Cliente(models.Model):
    SETOR_CHOICES = (
        ('Selecione', 'Selecione'),
        ('ASCOM', 'ASCOM'),
        ('ASPLAN', 'ASPLAN'),
        ('CAEIA', 'CAEIA'),
        ('CCA', 'CCA'),
        ('CCF', 'CCF'),
        ('CEA', 'CEA'),
        ('COMEG', 'COMEG'),
        ('COPAM', 'COPAM'),
        ('CPD', 'CPD'),
        ('CPL', 'CPL'),
        ('CRH', 'CRH'),
        ('CSG', 'CSG'),
        ('DA', 'DA'),
        ('DAO', 'DAO'),
        ('DIAT', 'DIAT'),
        ('DIFAU', 'DIFAU'),
        ('DIFLOR', 'DIFLOR'),
        ('DIMIN', 'DIMIN'),
        ('DINFRA', 'DINFRA'),
        ('DIPAP', 'DIPAP'),
        ('DS', 'DS'),
        ('DT', 'DT'),
        ('NOC', 'NOC'),
        ('PROJUR', 'PROJUR'),
        ('SETGEO', 'SETGEO'),
        ('SRS', 'SRS'),
        ('SUDCAR', 'SUDCAR'),
    )

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    setor = models.CharField(max_length=15, choices=SETOR_CHOICES, default='Selecione')
    placa_veiculo = models.CharField(max_length=15, unique=True)
    modelo_veiculo = models.CharField(max_length=15)
    
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    codigo_acesso = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    
    def __str__(self):
        return F"{self.nome} - {self.placa_veiculo}"



class RegistroAcesso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(auto_now=True)
    status_leitura = models.CharField(max_length=20, default='Entrada')


    def __str__(self):
        return F"{self.cliente.nome} - {self.data_entrada.strftime('%d/%m/%Y %H:%M')}"