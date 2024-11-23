from django.urls import path
from .views import *


urlpatterns = [
    path('criar/', CriarConsultaView.as_view(), name='criar_consulta'),
    path('consultas/', ListaConsultasView.as_view(), name='lista_consultas'),
]
