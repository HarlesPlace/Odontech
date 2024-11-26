from django.urls import path
from .views import *

app_name = 'consultas'

urlpatterns = [
    path('', ListaConsultasView.as_view(), name='lista_consultas'),
    path('agendar/', CriarConsultaView.as_view(), name='criar_consulta'),
    path('detalhes/<int:pk>/', ConsultaDetailView.as_view(), name='detalhes_consulta'), 
]
