from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import *
from .forms import *


class CriarPedidoView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = 'exames.add_pedido'
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


class PedidoUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    permission_required = 'exames.change_pedido'
    model = Pedido
    form_class = UpdatePedidoForm
    template_name = 'exames/editar_pedido.html'
    success_url = reverse_lazy('exames:lista_pedidos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['user'] = user  # Passando o usuário para o formulário
        return kwargs

    def get_object(self, queryset=None):
        # Obtém a consulta que será editada
        obj = super().get_object(queryset)

        # Verifica se o usuário tem permissão para editar a consulta
        if self.request.user == obj.cliente:
            raise Http404("Você não tem permissão para editar este pedido")
        
        return obj


class ListaPedidosView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = 'exames.view_pedido'
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
    

class PedidoDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    permission_required = 'exames.view_pedido'
    model = Pedido
    template_name = 'exames/detalhes_pedido.html'
    context_object_name = 'pedido'
