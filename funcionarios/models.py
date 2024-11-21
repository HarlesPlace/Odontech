from django.db import models
from contas.models import User
from clinicas.models import Endereco, Clinica

# Create your models here.
class Dentista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    cro = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_contratacao = models.DateField()
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)

class Secretario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    data_contratacao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    numero_residencial = models.CharField(max_length=10)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)


class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    data_contratacao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    numero_residencial = models.CharField(max_length=10)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)