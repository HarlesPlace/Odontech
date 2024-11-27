from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class CriarConsultaView(LoginRequiredMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/criar_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')


    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     user = self.request.user
        
    #     kwargs['initial'] = {'status': 'Agendada'}  # Preenche o campo status como agendada
    #     kwargs['disabled_fields'] = ['status']

    #     # Se o usuário for paciente
    #     if hasattr(user, 'cliente'):  # Verifica se o usuário tem um cliente associado
    #         kwargs['initial']['paciente'] = user.cliente # Preenche o campo paciente com o próprio paciente
    #         kwargs['disabled_fields'].append('paciente') # Desabilita o campo paciente
        
    #     # Se o usuário for dentista
    #     elif hasattr(user, 'dentista'):  # Verifica se o usuário tem um dentista associado
    #         kwargs['initial']['dentista'] = user.dentista  # Preenche o campo dentista com o próprio dentista
    #         kwargs['disabled_fields'].append('dentista') # Desabilita o campo dentista

    #     return kwargs
    
    

    # def form_valid(self, form):
    #     # Sempre que uma nova consulta for criada, o status será 'Agendada'
    #     form.instance.status = 'agendada'

    #     user = self.request.user
        
    #     # Verificando se o usuário é um dentista, secretário ou administrador
    #     if hasattr(user, 'dentista') or hasattr(user, 'secretario') or hasattr(user, 'administrador'):
    #         # O status pode ser alterado
    #         pass
    #     else:
    #         # Caso contrário, o status não pode ser alterado
    #         form.instance.status = 'agendada'

    #     return super().form_valid(form)
    
class ListaConsultasView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'consultas/lista_consultas.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        user = self.request.user

        
        if user.tipo_usuario == 'client':
            # Se for paciente, exibe somente suas consultas
            return Consulta.objects.filter(paciente=user.cliente)
        
        elif user.tipo_usuario == 'dentist':
            # Se for dentista, exibe as consultas onde ele é o dentista
            return Consulta.objects.filter(dentista=user.dentista)

        # Caso seja admin ou secretario, exibe todas as consultas
        return Consulta.objects.all()
    
class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'consultas/detalhes_consulta.html'
    context_object_name = 'consulta'