from django import forms
from .models import *
from pacientes.models import *
from funcionarios.models import *
from procedimentos.models import *

from django import forms
from .models import Cliente, Dentista, Consulta, Procedimento

class NomeModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'status', 'paciente', 'dentista', 'procedimentos']

    paciente = NomeModelChoiceField(
        queryset=Cliente.objects.all(),
        required=True,
        label="Paciente"
    )
    dentista = NomeModelChoiceField(
        queryset=Dentista.objects.all(),
        required=True,
        label="Dentista"
    )
    procedimentos = NomeModelChoiceField(
        queryset=Procedimento.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label="Procedimentos"
    )

    data = forms.DateField(widget=forms.SelectDateWidget, label="Data")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Hora")