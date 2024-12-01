from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import *
from .forms import *
from datetime import time,datetime,timedelta
import locale
import math
from funcionarios.forms import SelecionarDentistaForm
from pacientes.models import Cliente
from django.utils.dateparse import parse_datetime
#locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def iterar_horarios(data):
    inicio = datetime.combine(data, time(8, 0))  #Início às 08:00
    fim = datetime.combine(data, time(19, 30))  
    horario_atual = inicio
    while horario_atual <= fim:
        yield horario_atual
        horario_atual += timedelta(minutes=30)

class CriarConsultaView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = 'consultas.add_consulta'
    model = Consulta
    template_name = 'consultas/criar_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def get(self, request, pk=None):
        dentista=Dentista.objects.get(id=pk)
        dentistaform=SelecionarDentistaForm()
        form=self.get_form_class()
        calendario = {}
        dia = datetime.today().date()
        for i in range(15):
            if dia.weekday()!=6:
                calendario[dia.strftime('%d/%m (%a)')] = self.gerar_horarios(dia,dentista)
                dia += timedelta(days=1)
            else:
                calendario[dia.strftime('%d/%m (%a)')] = []
                dia += timedelta(days=1)
        return render(request, 'consultas/criar_consulta.html', {'form':form,'dentista':dentista,'calendario':calendario,'dentistaform':dentistaform})
    
    def post(self, request, pk):
        hora_selecionada = request.POST.get('hora')
        form_class = self.get_form_class()
        form = form_class(request.POST, user=request.user)

        if hora_selecionada:
            if form.is_valid():
                # Converte o horário para datetime
                horario = parse_datetime(hora_selecionada)
                dentista = Dentista.objects.get(id=pk)
                consulta = form.save(commit=False)
                consulta.status = 'agendada'
                consulta.paciente = Cliente.objects.get(usuario=self.request.user)
                consulta.dentista = dentista
                consulta.data = horario.date()  # Certifique-se que datahora é um datetime válido
                consulta.hora = horario.time()
                consulta.save()
                procedimento_especifico = Procedimento.objects.get(nome="Consulta") 
                consulta.procedimentos.add(procedimento_especifico)
                consulta.save()
            return redirect(self.success_url)
        else:
            return redirect('consultas:lista_consultas')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['user'] = user  # Passando o usuário para o formulário
        return kwargs
    
    def get_form_class(self):
        user = self.request.user
        # Verifica o tipo de usuário e escolhe o formulário correto
        if hasattr(user, 'cliente'):
            return ConsultaFormPaciente2  # Formulário para pacientes
        elif hasattr(user, 'dentista'):
            return ConsultaFormDentista  # Formulário para dentistas
        else:
            return ConsultaForm  # Formulário com todos os campos
        
    def gerar_horarios(self,data,dentista):
        inicio = datetime.combine(data, time(8, 0))  #Início às 08:00
        fim = datetime.combine(data, time(19, 30)) 
        horarios = []
        consultas=Consulta.objects.filter(dentista=dentista.id, data=data)
        restricoes=Restricao.objects.filter(dentista=dentista.id, data=data)
        while inicio <= fim:
            if restricoes:
                for restricao in restricoes:
                    inicio_dt = datetime.combine(data, inicio.time())  # Combina com a data atual
                    restricao_dt = datetime.combine(data, restricao.hora_inicio)  # O mesmo para a hora de restrição
                    # Calcula a diferença
                    diferenca = abs(inicio_dt - restricao_dt)
                    if inicio.time()==restricao.hora_inicio or (diferenca <= timedelta(minutes=15)):
                        inicio += abs(datetime.combine(data, restricao.hora_inicio)-datetime.combine(data,restricao.hora_fim))
            if consultas:
                for consulta in (consultas):
                    if inicio.time()!=consulta.hora:
                        horarios.append(inicio)
                        inicio += timedelta(minutes=30)       
                    else:
                        procedimentosConsulta=consulta.procedimentos.all()
                        if procedimentosConsulta:
                            duracao_total = sum([proc.duracao_media.total_seconds() for proc in procedimentosConsulta])
                            duracao_arredondada = math.ceil(duracao_total / (15 * 60)) * 15 * 60
                            inicio += timedelta(seconds=duracao_arredondada)
                        else:
                            inicio += timedelta(minutes=30)   

            else:
                horarios.append(inicio)
                inicio += timedelta(minutes=30)
        return horarios
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ConsultaUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    permission_required = 'consultas.change_consulta'
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
 
class ListaConsultasView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = 'consultas.view_consulta'
    model = Consulta
    template_name = 'consultas/lista_consultas.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        user = self.request.user

        
        if user.tipo_usuario == 'client':
            # Se for paciente, exibe somente suas consultas
            return Consulta.objects.filter(paciente=user.cliente).order_by('-data','-hora')
        
        elif user.tipo_usuario == 'dentist':
            # Se for dentista, exibe as consultas onde ele é o dentista
            return Consulta.objects.filter(dentista=user.dentista).order_by('-data','-hora')

        # Caso seja admin ou secretario, exibe todas as consultas
        return Consulta.objects.all()
    
class ConsultaDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    permission_required = 'consultas.view_consulta'
    model = Consulta
    template_name = 'consultas/detalhes_consulta.html'
    context_object_name = 'consulta'

def SelecionaDentistaView(request):
    if request.method == 'GET':
        try:
            form = SelecionarDentistaForm(request.GET)
            if form.is_valid():
                pk = form.cleaned_data['dentista'].id
                return redirect('consultas:criar_consulta', pk=pk)
            else:
                dentista=Dentista.objects.first()
                return redirect('consultas:criar_consulta', pk=dentista.id)
        except:
            dentista=Dentista.objects.first()
            return redirect('consultas:criar_consulta', pk=dentista.id)

class CriarConsultaDentistaView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = 'consultas.add_consulta'
    model = Consulta
    template_name = 'consultas/criar_consultaDentista.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def get(self, request, pk=None):
        cliente=Cliente.objects.get(id=pk)
        dentista=Dentista.objects.get(usuario=self.request.user)
        #dentistaform=SelecionarDentistaForm()
        form=self.get_form_class()
        calendario = {}
        dia = datetime.today().date()
        for i in range(15):
            if dia.weekday()!=6:
                calendario[dia.strftime('%d/%m (%a)')] = self.gerar_horarios(dia,dentista)
                dia += timedelta(days=1)
            else:
                calendario[dia.strftime('%d/%m (%a)')] = []
                dia += timedelta(days=1)
        return render(request, 'consultas/criar_consultaDentista.html', {'form':form,'dentista':dentista,'calendario':calendario,'cliente':cliente})
    
    def post(self, request, pk):
        hora_selecionada = request.POST.get('hora')
        form_class = self.get_form_class()
        form = form_class(request.POST, user=request.user)

        if hora_selecionada:
            if form.is_valid():
                # Converte o horário para datetime
                horario = parse_datetime(hora_selecionada)
                cliente = Cliente.objects.get(id=pk)
                consulta = form.save(commit=False)
                consulta.status = 'agendada'
                consulta.paciente = cliente
                consulta.dentista = Dentista.objects.get(usuario=self.request.user)
                consulta.data = horario.date()  # Certifique-se que datahora é um datetime válido
                consulta.hora = horario.time()
                consulta.save()
            return redirect("consultas:editar_consulta", pk=consulta.pk)
        else:
            return redirect('consultas:lista_consultas')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['user'] = user  # Passando o usuário para o formulário
        return kwargs
    
    def get_form_class(self):
        user = self.request.user
        # Verifica o tipo de usuário e escolhe o formulário correto
        if hasattr(user, 'cliente'):
            return ConsultaFormPaciente2  # Formulário para pacientes
        elif hasattr(user, 'dentista'):
            return ConsultaFormDentista2  # Formulário para dentistas
        else:
            return ConsultaForm  # Formulário com todos os campos
        
    def gerar_horarios(self,data,dentista):
        inicio = datetime.combine(data, time(8, 0))  #Início às 08:00
        fim = datetime.combine(data, time(19, 30)) 
        horarios = []
        consultas=Consulta.objects.filter(dentista=dentista.id, data=data)
        restricoes=Restricao.objects.filter(dentista=dentista.id, data=data)
        while inicio <= fim:
            if restricoes:
                for restricao in restricoes:
                    inicio_dt = datetime.combine(data, inicio.time())  # Combina com a data atual
                    restricao_dt = datetime.combine(data, restricao.hora_inicio)  # O mesmo para a hora de restrição
                    # Calcula a diferença
                    diferenca = abs(inicio_dt - restricao_dt)
                    if inicio.time()==restricao.hora_inicio or (diferenca <= timedelta(minutes=15)):
                        inicio += abs(datetime.combine(data, restricao.hora_inicio)-datetime.combine(data,restricao.hora_fim))
            if consultas:
                for consulta in (consultas):
                    if inicio.time()!=consulta.hora:
                        horarios.append(inicio)
                        inicio += timedelta(minutes=30)       
                    else:
                        procedimentosConsulta=consulta.procedimentos.all()
                        if procedimentosConsulta:
                            duracao_total = sum([proc.duracao_media.total_seconds() for proc in procedimentosConsulta])
                            duracao_arredondada = math.ceil(duracao_total / (15 * 60)) * 15 * 60
                            inicio += timedelta(seconds=duracao_arredondada)
                        else:
                            inicio += timedelta(minutes=30)   
            else:
                horarios.append(inicio)
                inicio += timedelta(minutes=30)
        return horarios
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
