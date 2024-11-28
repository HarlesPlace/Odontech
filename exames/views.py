from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class CriarPedidoView(LoginRequiredMixin, CreateView):
    model = Pedido
    template_name = 'exames/criar_pedido.html'
    success_url = reverse_lazy('exames:lista_pedidos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        
        kwargs['user'] = user  # Passando o usuário para o formulário
        
        return kwargs
    
    def get_form_class(self):
        user = self.request.user

        # Verifica o tipo de usuário e escolhe o formulário correto
        if hasattr(user, 'dentista'):
            return PedidoFormDentista  # Formulário para dentistas
        
        else:
            return PedidoForm  # Formulário com todos os campos


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
