from django.db import models
from contas.models import User


class Cliente(models.Model):
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

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome=models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True,null=True)
    telefone = models.CharField(max_length=15,null=True)
    data_nascimento = models.DateField(null=True)
    plano_saude = models.CharField(max_length=100, null=True, blank=True)
    historico_clinico = models.TextField(null=True)
    rua = models.CharField(max_length=100,null=True)
    bairro = models.CharField(max_length=100,null=True)
    cep = models.CharField(max_length=15,null=True)
    cidade = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=2,choices=ESTADOS_CHOICES, default='SP')
    ultima_atualizacao = models.DateTimeField(auto_now=True,null=True)
    numero_residencial = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.nome