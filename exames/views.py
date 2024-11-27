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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user

        kwargs['initial'] = {'status': 'pendente'}  # Preenche o campo status como 'pendente'
        kwargs['disabled_fields'] = ['status']

        # Se o usuário for paciente
        if hasattr(user, 'cliente'):  # Verifica se o usuário tem um cliente associado
            kwargs['initial']['cliente'] = user.cliente  # Preenche o campo cliente com o próprio cliente
            kwargs['disabled_fields'].append('cliente')  # Desabilita o campo 'cliente'

        # Se o usuário for dentista
        elif hasattr(user, 'dentista'):  # Verifica se o usuário tem um dentista associado
            kwargs['initial']['dentista'] = user.dentista  # Preenche o campo dentista com o próprio dentista
            kwargs['disabled_fields'].append('dentista')  # Desabilita o campo 'dentista'

        return kwargs

    def form_valid(self, form):
        # Garantir que o status esteja 'pendente' quando um novo pedido for criado
        form.instance.status = 'pendente'

        user = self.request.user

        # Se o usuário for dentista, secretário ou administrador, ele pode alterar o status
        if hasattr(user, 'dentista') or hasattr(user, 'secretario') or hasattr(user, 'administrador'):
            pass  # O status pode ser alterado

        # Caso contrário, o status permanece 'pendente'
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
