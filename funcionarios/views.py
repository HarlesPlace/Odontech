from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Dentista,Secretario
from contas.models import User
from .forms import DentistaForm, UserDentistaRegistrationForm, SecretarioForm, UserSecretarioRegistrationForm

class CreateUserDentista(generic.CreateView):
    model=User
    template_name="funcionarios/createUserDentista.html"
    form_class=UserDentistaRegistrationForm
    def get_success_url(self):
        dentista = Dentista.objects.get(usuario=self.object.pk)
        return reverse('funcionarios:updateDentista',args=[dentista.pk])

class CreateDentista(generic.CreateView):
    model=Dentista
    template_name="funcionarios/createDentista.html"
    form_class=DentistaForm
    def get_success_url(self):
        return reverse('funcionarios:detailDentista', args=[self.object.pk])
       
class UpdateDentista(generic.UpdateView):
    model= Dentista
    template_name="funcionarios/updateDentista.html"
    form_class=DentistaForm
    def get_success_url(self):
        return reverse('funcionarios:detailDentista', args=[self.object.pk])

class DeleteDentista(generic.DeleteView):
    model=Dentista
    template_name="funcionarios/deleteDentista.html"
    def get_success_url(self):
        return reverse('funcionarios:indexDentista')
    
class ListDentista(generic.ListView):
    model=Dentista
    template_name='funcionarios/indexDentista.html'

class DetailDentista(generic.DetailView):
    model=Dentista
    template_name='funcionarios/detailDentista.html'

def searchDentista(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        dentista_list = Dentista.objects.filter(titulo__icontains=search_term)
        context = {"dentista_list": dentista_list}
    return render(request, 'funcionarios/searchDentista.html', context)

class CreateUserSecretario(generic.CreateView):
    model=User
    template_name="funcionarios/createUserSecretario.html"
    form_class=UserSecretarioRegistrationForm
    def get_success_url(self):
        secretario = Secretario.objects.get(usuario=self.object.pk)
        return reverse('funcionarios:updateSecretario',args=[secretario.pk])

class CreateSecretario(generic.CreateView):
    model=Secretario
    template_name="funcionarios/createSecretario.html"
    form_class=SecretarioForm
    def get_success_url(self):
        return reverse('funcionarios:detailSecretario', args=[self.object.pk])
       
class UpdateSecretario(generic.UpdateView):
    model= Secretario
    template_name="funcionarios/updateSecretario.html"
    form_class=SecretarioForm
    def get_success_url(self):
        return reverse('funcionarios:detailSecretario', args=[self.object.pk])

class DeleteSecretario(generic.DeleteView):
    model=Secretario
    template_name="funcionarios/deleteSecretario.html"
    def get_success_url(self):
        return reverse('funcionarios:indexSecretario')
    
class ListSecretario(generic.ListView):
    model=Secretario
    template_name='funcionarios/indexSecretario.html'

class DetailSecretario(generic.DetailView):
    model=Secretario
    template_name='funcionarios/detailSecretario.html'

def searchSecretario(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        secretario_list = Dentista.objects.filter(titulo__icontains=search_term)
        context = {"secretario_list": secretario_list}
    return render(request, 'funcionarios/searchSecretario.html', context)