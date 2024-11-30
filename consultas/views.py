from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from datetime import time,datetime,timedelta
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def iterar_horarios(data):
    inicio = datetime.combine(data, time(8, 0))  #Início às 08:00
    fim = datetime.combine(data, time(19, 30))  
    horario_atual = inicio
    while horario_atual <= fim:
        yield horario_atual
        horario_atual += timedelta(minutes=30)

def gerar_horarios(data):
    inicio = datetime.combine(data, time(8, 0))  #Início às 08:00
    fim = datetime.combine(data, time(19, 30)) 
    horarios = []
    while inicio <= fim:
        horarios.append(inicio.strftime('%H:%M'))
        inicio += timedelta(minutes=30)
    return horarios

class CriarConsultaView(LoginRequiredMixin, CreateView):
    model = Consulta
    template_name = 'consultas/criar_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        
        kwargs['user'] = user  # Passando o usuário para o formulário
        
        return kwargs
    
    def get_form_class(self):
        user = self.request.user

        # Verifica o tipo de usuário e escolhe o formulário correto
        if hasattr(user, 'cliente'):
            return ConsultaFormPaciente  # Formulário para pacientes
        
        elif hasattr(user, 'dentista'):
            return ConsultaFormDentista  # Formulário para dentistas
        
        else:
            return ConsultaForm  # Formulário com todos os campos
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendario = {}
        dia = datetime.today().date()

        for i in range(15):
            if dia.weekday()!=6:
                calendario[dia.strftime('%d/%m (%a)')] = gerar_horarios(dia)
                dia += timedelta(days=1)
            else:
                calendario[dia.strftime('%d/%m (%a)')] = []
                dia += timedelta(days=1)
        context['calendario'] = calendario
        return context

class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/edita_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['user'] = user  # Passando o usuário para o formulário
        return kwargs

    def get_object(self, queryset=None):
        # Obtém a consulta que será editada
        obj = super().get_object(queryset)

        # Verifica se o usuário tem permissão para editar a consulta
        if self.request.user == obj.paciente:
            raise Http404("Você não tem permissão para editar esta consulta")
        
        return obj
 
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