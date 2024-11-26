from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Procedimento
from .forms import ProcedimentoForm

class CreateProcedimento(generic.CreateView):
    model=Procedimento
    template_name="procedimentos/createProcedimento.html"
    form_class=ProcedimentoForm
    def get_success_url(self):
        return reverse('procedimentos:detailProcedimento', args=[self.object.pk])
       
class UpdateProcedimento(generic.UpdateView):
    model= Procedimento
    template_name="procedimentos/updateProcedimento.html"
    form_class=ProcedimentoForm
    def get_success_url(self):
        return reverse('procedimentos:detailProcedimento', args=[self.object.pk])

class DeleteProcedimento(generic.DeleteView):
    model=Procedimento
    template_name="procedimentos/deleteProcedimento.html"
    def get_success_url(self):
        return reverse('procedimentos:indexProcedimento')
    
class ListProcedimento(generic.ListView):
    model=Procedimento
    template_name='procedimentos/indexProcedimento.html'

class DetailProcedimento(generic.DetailView):
    model=Procedimento
    template_name='procedimentos/detailProcedimento.html'

def searchProcedimento(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        procedimento_list = Procedimento.objects.filter(titulo__icontains=search_term)
        context = {"procedimento_list": procedimento_list}
    return render(request, 'procedimentos/searchProcedimento.html', context)