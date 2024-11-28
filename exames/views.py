from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class CriarPedidoView(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'exames/criar_pedido.html'
    success_url = reverse_lazy('exames:lista_pedidos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user

        # Inicializa o campo de status com 'pendente'
        kwargs['initial'] = {'status': 'pendente'}  
        kwargs['disabled_fields'] = ['status']

        # Se o usuário for paciente, preenche automaticamente o campo cliente com o cliente associado
        if hasattr(user, 'cliente'):
            kwargs['initial']['cliente'] = user.cliente
            kwargs['disabled_fields'].append('cliente')

        # Se o usuário for dentista, preenche automaticamente o campo dentista com o dentista associado
        elif hasattr(user, 'dentista'):
            kwargs['initial']['dentista'] = user.dentista
            kwargs['disabled_fields'].append('dentista')

        return kwargs

    def form_valid(self, form):
        # Sempre que o pedido for validado, o status será 'pendente'
        form.instance.status = 'pendente'
        
        user = self.request.user

        # Verificando se o usuário é dentista, secretário ou administrador
        if hasattr(user, 'dentista') or hasattr(user, 'secretario') or hasattr(user, 'administrador'):
            pass  # O status pode ser alterado
        
        # Se não, o status permanece 'pendente'
        else:
            form.instance.status = 'pendente'

        return super().form_valid(form)
    
    

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
