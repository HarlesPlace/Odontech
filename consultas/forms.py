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
        fields = ['data', 'hora', 'dentista','paciente']

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
    
    #procedimentos = forms.ModelMultipleChoiceField(
        #queryset=Procedimento.objects.all(),
        #required=True,
        #widget=forms.CheckboxSelectMultiple,
        #label="Procedimentos"
    #)

    data = forms.DateField(widget=forms.SelectDateWidget, label="Data")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Hora")

    def save(self,commit=True):
        consulta=super().save(commit=False)
        #consulta.paciente = Cliente.objects.get(usuario_id=self.user.id)
        consulta.status='agendada'
        if commit: 
            consulta.save()
            # Associa o procedimento automaticamente para cliente, deixem um procedimento "Consulta" no bd de vcs
            procedimento_especifico = Procedimento.objects.get(nome="Consulta") 
            consulta.procedimentos.add(procedimento_especifico)
            # ---------- jeito que funciona pra cadastrar n2n--------------------------
            #if 'procedimentos' in self.cleaned_data:
                #procedimentos = self.cleaned_data['procedimentos']
                #consulta.procedimentos.set(procedimentos)  # Associa os procedimentos selecionados à consulta
        return consulta