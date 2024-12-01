from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Dentista,Secretario
from contas.models import User
from consultas.models import Restricao
from .forms import DentistaForm, UserDentistaRegistrationForm, SecretarioForm, UserSecretarioRegistrationForm, RestricaoDentistaForm
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class CreateUserDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    permission_required = 'funcionarios.add_dentista'
    model=User
    template_name="funcionarios/createUserDentista.html"
    form_class=UserDentistaRegistrationForm
    def get_success_url(self):
        dentista = Dentista.objects.get(usuario=self.object.pk)
        return reverse('funcionarios:updateDentista',args=[dentista.pk])

class CreateDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    permission_required = 'funcionarios.add_dentista'
    model=Dentista
    template_name="funcionarios/createDentista.html"
    form_class=DentistaForm
    def get_success_url(self):
        return reverse('funcionarios:detailDentista', args=[self.object.pk])
       
class UpdateDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    permission_required = 'funcionarios.change_dentista'
    model= Dentista
    template_name="funcionarios/updateDentista.html"
    form_class=DentistaForm
    def get_success_url(self):
        return reverse('funcionarios:detailDentista', args=[self.object.pk])

class DeleteDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    permission_required = 'funcionarios.delete_dentista'
    model=Dentista
    template_name="funcionarios/deleteDentista.html"
    def get_success_url(self):
        return reverse('funcionarios:indexDentista')
    
class ListDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    permission_required = 'funcionarios.view_dentista'
    model=Dentista
    template_name='funcionarios/indexDentista.html'

class DetailDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    permission_required = 'funcionarios.view_dentista'
    model=Dentista
    template_name='funcionarios/detailDentista.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restricao_list = Restricao.objects.filter(dentista=self.object.pk,data__gte=date.today()).order_by('data','hora_inicio')
        context['restricao_list'] = restricao_list
        return context

def searchDentista(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        dentista_list = Dentista.objects.filter(nome__icontains=search_term)
        context = {"dentista_list": dentista_list}
    return render(request, 'funcionarios/searchDentista.html', context)

class CreateUserSecretario(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    permission_required = 'funcionarios.add_secretario'
    model=User
    template_name="funcionarios/createUserSecretario.html"
    form_class=UserSecretarioRegistrationForm
    def get_success_url(self):
        secretario = Secretario.objects.get(usuario=self.object.pk)
        return reverse('funcionarios:updateSecretario',args=[secretario.pk])

class CreateSecretario(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    permission_required = 'funcionarios.add_secretario'
    model=Secretario
    template_name="funcionarios/createSecretario.html"
    form_class=SecretarioForm
    def get_success_url(self):
        return reverse('funcionarios:detailSecretario', args=[self.object.pk])
       
class UpdateSecretario(LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    permission_required = 'funcionarios.change_secretario'
    model= Secretario
    template_name="funcionarios/updateSecretario.html"
    form_class=SecretarioForm
    def get_success_url(self):
        return reverse('funcionarios:detailSecretario', args=[self.object.pk])

class DeleteSecretario(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    permission_required = 'funcionarios.delete_secretario'
    model=Secretario
    template_name="funcionarios/deleteSecretario.html"
    def get_success_url(self):
        return reverse('funcionarios:indexSecretario')
    
class ListSecretario(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    permission_required = 'funcionarios.view_secretario'
    model=Secretario
    template_name='funcionarios/indexSecretario.html'

class DetailSecretario(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    permission_required = 'funcionarios.view_secretario'
    model=Secretario
    template_name='funcionarios/detailSecretario.html'

def searchSecretario(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        secretario_list = Dentista.objects.filter(nome__icontains=search_term)
        context = {"secretario_list": secretario_list}
    return render(request, 'funcionarios/searchSecretario.html', context)

class CreateRestricaoDentista(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    permission_required = 'consultas.add_restricao'
    model=Restricao
    template_name="funcionarios/createRestricaoDentista.html"
    def get(self, request, pk):
        dentista=get_object_or_404(Dentista, id=pk)
        form = RestricaoDentistaForm()
        return render(request, 'funcionarios/createRestricaoDentista.html', {'form': form,'dentista':dentista})
    
    def post(self, request,pk):
        form = RestricaoDentistaForm(request.POST)
        if form.is_valid():
            restricao = form.save(commit=False)
            dentista=get_object_or_404(Dentista, id=pk)
            # Associa o dentista à restrição
            restricao.dentista= dentista
            # Salva a restrição
            restricao.save()
            return render(request, 'funcionarios/detailDentista.html', {'form': form,'dentista':dentista})
        return render(request, 'funcionarios/createRestricaoDentista.html', {'form': form})
    
    #def get_success_url(self):
        #return reverse('funcionarios:detailDentista',args=[self.object.dentista.pk])

class DeleteRestricao(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    permission_required = 'consultas.delete_restricao'
    model = Restricao
    def get_success_url(self):
        # Redireciona para a página de detalhes do dentista após a exclusão
        return reverse('funcionarios:detailDentista', kwargs={'pk': self.object.dentista.pk})