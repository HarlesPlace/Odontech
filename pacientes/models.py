from django.db import models
from clinicas.models import Endereco
from contas.models import User

# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    plano_saude = models.CharField(max_length=100, null=True, blank=True)
    historico_clinico = models.TextField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)