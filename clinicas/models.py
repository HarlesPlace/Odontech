from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)