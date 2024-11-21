from django.db import models
from pacientes.models import Cliente
from funcionarios.models import Dentista
from procedimentos.models import Procedimento


# Create your models here.
class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=[('agendada', 'Agendada'), ('suspensa', 'Suspensa'), ('concluída', 'Concluída')])
    paciente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    procedimentos=models.ManyToManyField(Procedimento)

class Restricao(models.Model):
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()