from django import forms
from .models import *
from pacientes.models import *
from funcionarios.models import *
from procedimentos.models import *
from .models import *



class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'dentista','paciente', 'procedimentos']

    paciente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        required=True,
        label="Paciente"
    )
    dentista = forms.ModelChoiceField(
        queryset=Dentista.objects.all(),
        required=True,
        label="Dentista"
    )
    procedimentos = forms.ModelMultipleChoiceField(
        queryset=Procedimento.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label="Procedimentos"
    )

    data = forms.DateField(widget=forms.SelectDateWidget, label="Data")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Hora")

    def save(self,commit=True):
        consulta=super().save(commit=False)
        #consulta.paciente = Cliente.objects.get(usuario_id=self.user.id)
        consulta.status='agendada'
        if commit: 
            consulta.save()
        return consulta

    def __init__(self, *args, **kwargs):
        # Pega os argumentos do view para verificar se devemos desabilitar campos
        disabled_fields = kwargs.pop('disabled_fields', [])
        super().__init__(*args, **kwargs)

        # Desabilita os campos conforme necessário
        for field in disabled_fields:
            if field in self.fields:
                self.fields[field].widget.attrs['disabled'] = 'disabled'
                self.fields[field].required = False  # Torna o campo não obrigatório