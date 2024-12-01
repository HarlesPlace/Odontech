from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import generic
from .forms import ClienteForm
from django.urls import reverse

# Create your views here.

class UpdateCliente(LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    permission_required = 'pacientes.change_cliente'
    model= Cliente
    template_name="pacientes/updatePaciente.html"
    form_class=ClienteForm
    def get_success_url(self):
        return reverse('pacientes/detailPaciente.html', args=[self.object.pk])
    
class DetailCliente(LoginRequiredMixin, PermissionRequiredMixin,generic.DetailView):
    permission_required = 'pacientes.view_cliente'
    model=Cliente
    template_name='pacientes/detailPaciente.html'