from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=50, 
                                    choices=[('admin', 'Administrador'), 
                                             ('dentist', 'Dentista'), 
                                             ('client', 'Cliente'), 
                                             ('secretary', 'Secretário')])
    
    status = models.CharField(max_length=20, 
                              choices=[('active', 'Ativo'), 
                                       ('inactive', 'Inativo')], 
                                       default='active')
    
    data_criacao = models.DateField(auto_now_add=True)
    data_ultimo_login = models.DateTimeField(null=True, blank=True)
# Create your models here.
