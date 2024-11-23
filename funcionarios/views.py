#from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Dentista
from contas.models import User
from .forms import DentistaForm, UserDentistaRegistrationForm

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

