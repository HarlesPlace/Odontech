from django import forms
from .models import *
from pacientes.models import *
from funcionarios.models import *
from procedimentos.models import *

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'status', 'paciente', 'dentista', 'procedimentos']

    paciente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)
    dentista = forms.ModelChoiceField(queryset=Dentista.objects.all(), required=True)
    procedimentos = forms.ModelMultipleChoiceField(queryset=Procedimento.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)

    data = forms.DateField(widget=forms.SelectDateWidget)
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
