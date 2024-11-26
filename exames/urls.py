from django.urls import path
from .views import *

app_name = 'exames'

urlpatterns = [
    path('', ListaPedidosView.as_view(), name='lista_pedidos'),
    path('agendar/', CriarPedidoView.as_view(), name='criar_pedido'),
    path('detalhes/<int:pk>/', PedidoDetailView.as_view(), name='detalhes_pedido'),
]
