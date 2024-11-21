from django.contrib import admin
from .models import *

r = admin.site.register #Mais fácil de escrever assim

r(Exame)
r(Pedido)
