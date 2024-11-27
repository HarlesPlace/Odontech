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

    def __init__(self, *args, **kwargs):
        # Pega os argumentos do view para verificar se devemos desabilitar campos
        disabled_fields = kwargs.pop('disabled_fields', [])
        super().__init__(*args, **kwargs)

        # Desabilita os campos conforme necessário
        for field in disabled_fields:
            if field in self.fields:
                self.fields[field].widget.attrs['disabled'] = 'disabled'
                self.fields[field].required = False  # Torna o campo não obrigatório