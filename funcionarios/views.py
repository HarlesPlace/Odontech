from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Dentista
from .forms import DentistaForm

class CreatDentista(generic.CreateView):
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

