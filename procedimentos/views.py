from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Procedimento
from .forms import ProcedimentoForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class CreateProcedimento(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    permission_required = 'procedimentos.add_procedimento'
    model=Procedimento
    template_name="procedimentos/createProcedimento.html"
    form_class=ProcedimentoForm
    def get_success_url(self):
        return reverse('procedimentos:detailProcedimento', args=[self.object.pk])
       
class UpdateProcedimento(LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    permission_required = 'procedimentos.change_procedimento'
    model= Procedimento
    template_name="procedimentos/updateProcedimento.html"
    form_class=ProcedimentoForm
    def get_success_url(self):
        return reverse('procedimentos:detailProcedimento', args=[self.object.pk])

class DeleteProcedimento(LoginRequiredMixin, PermissionRequiredMixin,generic.DeleteView):
    permission_required = 'procedimentos.delete_procedimento'
    model=Procedimento
    template_name="procedimentos/deleteProcedimento.html"
    def get_success_url(self):
        return reverse('procedimentos:indexProcedimento')
    
class ListProcedimento(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    permission_required = 'procedimentos.view_procedimento'
    model=Procedimento
    template_name='procedimentos/indexProcedimento.html'

class DetailProcedimento(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    permission_required = 'procedimentos.view_procedimento'
    model=Procedimento
    template_name='procedimentos/detailProcedimento.html'

def searchProcedimento(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        procedimento_list = Procedimento.objects.filter(titulo__icontains=search_term)
        context = {"procedimento_list": procedimento_list}
    return render(request, 'procedimentos/searchProcedimento.html', context)