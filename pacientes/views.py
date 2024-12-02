from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import generic
from .forms import ClienteForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render

# Create your views here.

class UpdateCliente(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'pacientes.change_cliente'
    model = Cliente
    template_name = "pacientes/updateCliente.html"
    form_class = ClienteForm

    def get_success_url(self):
        # Use o nome correto do URL com o namespace
        return reverse_lazy('pacientes:detailCliente', args=[self.object.pk])

    
class DetailCliente(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    permission_required = 'pacientes.view_cliente'
    model=Cliente
    template_name='pacientes/detailCliente.html'

class ListCliente(LoginRequiredMixin, PermissionRequiredMixin,generic.ListView):
    permission_required = 'pacientes.view_cliente'
    model=Cliente
    template_name='pacientes/indexCliente.html'

def searchCliente(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        cliente_list = Cliente.objects.filter(nome__icontains=search_term)
        print("--------------------------")
        print(cliente_list)
        context = {"cliente_list": cliente_list}
    return render(request, 'pacientes/searchCliente.html', context)