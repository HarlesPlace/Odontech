from django.db import models
from pacientes.models import Cliente
from funcionarios.models import Dentista


# Create your models here.
class Exame(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    status = models.CharField(max_length=20)
    link_resultado = models.URLField(null=True, blank=True)
    exames=models.ManyToManyField(Exame)