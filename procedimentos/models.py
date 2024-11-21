from django.db import models

# Create your models here.
class Procedimento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_media = models.DurationField()

class ListProcedimentosConsulta(models.Model):
    consulta = models.ForeignKey('appointments.Consulta', on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)