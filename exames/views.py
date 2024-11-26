from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class CriarPedidoView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'exames/criar_pedido.html'
    success_url = reverse_lazy('exames:lista_pedidos')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ListaPedidosView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'exames/lista_pedidos.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        user = self.request.user
        
        if user.tipo_usuario == 'client':
            # Se for paciente, exibe somente seus pedidos de exames
            return Pedido.objects.filter(cliente=user.cliente)
        
        elif user.tipo_usuario == 'dentist':
            # Se for dentista, exibe os pedidos em que ele é o dentista
            return Pedido.objects.filter(dentista=user.dentista)

        # Caso seja admin ou secretario, exibe todos os pedidos
        return Pedido.objects.all()
    

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'exames/detalhes_pedido.html'
    context_object_name = 'pedido'
