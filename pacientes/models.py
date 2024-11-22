from django.db import models
from clinicas.models import Endereco
from contas.models import User

# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome=models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True,null=True)
    telefone = models.CharField(max_length=15,null=True)
    data_nascimento = models.DateField(null=True)
    plano_saude = models.CharField(max_length=100, null=True, blank=True)
    historico_clinico = models.TextField(null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    numero_residencial = models.CharField(max_length=10,null=True)