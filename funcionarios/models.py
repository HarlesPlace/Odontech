from django.db import models
from contas.models import User
from clinicas.models import Clinica
ESTADOS_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
# Create your models here.
class Dentista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True,null=True)
    cro = models.CharField(max_length=20, unique=True,null=True)
    especialidade = models.CharField(max_length=100,null=True)
    telefone = models.CharField(max_length=15,null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    data_contratacao = models.DateField(null=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE,null=True)
    rua = models.CharField(max_length=100,null=True)
    bairro = models.CharField(max_length=100,null=True)
    cep = models.CharField(max_length=15,null=True)
    cidade = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=2,choices=ESTADOS_CHOICES, default='SP',null=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True,null=True)
    numero_residencial = models.CharField(max_length=10,null=True)
    def delete(self, *args, **kwargs):
        # Deleta o usuário associado antes de deletar o dentista
        self.usuario.delete()
        super().delete(*args, **kwargs)

class Secretario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True,null=True)
    telefone = models.CharField(max_length=15,null=True)
    data_contratacao = models.DateField(null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    numero_residencial = models.CharField(max_length=10,null=True)
    rua = models.CharField(max_length=100,null=True)
    bairro = models.CharField(max_length=100,null=True)
    cep = models.CharField(max_length=15,null=True)
    cidade = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=2,choices=ESTADOS_CHOICES, default='SP',null=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True,null=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE,null=True)
    def delete(self, *args, **kwargs):
        # Deleta o usuário associado antes de deletar o secretário
        self.usuario.delete()
        super().delete(*args, **kwargs)

class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    data_contratacao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    numero_residencial = models.CharField(max_length=10)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2,choices=ESTADOS_CHOICES, default='SP')
    ultima_atualizacao = models.DateTimeField(auto_now=True,null=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)