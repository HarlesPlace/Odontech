from django.urls import path
from .views import *

app_name = 'consultas'

urlpatterns = [
    path('', ListaConsultasView.as_view(), name='lista_consultas'),
    path('agendar/<int:pk>/dentista/', CriarConsultaDentistaView.as_view(), name='Dentistacriar_consulta'),
    path('agendar/<int:pk>/', CriarConsultaView.as_view(), name='criar_consulta'),
    path('agendar/selecionaDent/', SelecionaDentistaView, name='selecionaDentista'),
    path('detalhes/<int:pk>/', ConsultaDetailView.as_view(), name='detalhes_consulta'), 
    path('editar/<int:pk>/', ConsultaUpdateView.as_view(), name='editar_consulta'),
]
