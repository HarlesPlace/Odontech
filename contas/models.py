from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','email']
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
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=150)

    def __str__(self):
        return self.first_name+" "+self.last_name

