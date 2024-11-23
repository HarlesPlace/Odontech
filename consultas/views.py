from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *

class CriarConsultaView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/criar_consulta.html'
    success_url = reverse_lazy('consultas:lista_consultas')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class ListaConsultasView(ListView):
    model = Consulta
    template_name = 'consultas/lista_consultas.html'
    context_object_name = 'consultas'
    paginate_by = 10  

    def get_queryset(self):

        return Consulta.objects.all().order_by('-data', '-hora')
