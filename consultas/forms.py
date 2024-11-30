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
        queryset = Cliente.objects.all(),
        required = True,
        label = "Paciente"
    )
    
    dentista = forms.ModelChoiceField(
        queryset = Dentista.objects.all(),
        required = True,
        label = "Dentista"
    )

    procedimentos = forms.ModelMultipleChoiceField(
        queryset = Procedimento.objects.all(),
        required = True,
        widget = forms.CheckboxSelectMultiple,
        label = "Procedimentos"
    )

    data = forms.DateField(widget=forms.SelectDateWidget, label="Data")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Hora")

    def save(self,commit=True):
        consulta=super().save(commit=False)
                
        consulta.status='agendada'

        if commit: 
            consulta.save()

            procedimentos_selecionados = self.cleaned_data['procedimentos']
            consulta.procedimentos.set(procedimentos_selecionados)
            
            # ---------- jeito que funciona pra cadastrar n2n--------------------------
            #if 'procedimentos' in self.cleaned_data:
                #procedimentos = self.cleaned_data['procedimentos']
                #consulta.procedimentos.set(procedimentos)  # Associa os procedimentos selecionados à consulta
        return consulta

    def __init__(self, *args, **kwargs):
        # Por mais que não seja usado nesse form, tem que ter isso pra não bugar
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


class ConsultaFormPaciente(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'dentista']

    dentista = forms.ModelChoiceField(
        queryset = Dentista.objects.all(),
        required = True,
        label = "Dentista"
    )

    data = forms.DateField(widget=forms.SelectDateWidget, label="Data")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Hora")

    def save(self,commit=True):
        consulta = super().save(commit=False)
        
        consulta.status = 'agendada'
        consulta.paciente = self.user.cliente

        if commit: 
            consulta.save()

            # Associa o procedimento automaticamente para cliente, deixem um procedimento "Consulta" no bd de vcs
            procedimento_especifico = Procedimento.objects.get(nome="Consulta") 
            consulta.procedimentos.add(procedimento_especifico)
        
        return consulta
    
    def __init__(self, *args, **kwargs):
        # Pega o usuário da view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class ConsultaFormPaciente2(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = []
    dentista=forms.HiddenInput
    data = forms.HiddenInput
    hora = forms.HiddenInput
    status = forms.HiddenInput
    paciente = forms.HiddenInput
    procedimentos=forms.HiddenInput
    
    def __init__(self, *args, **kwargs):
        # Pega o usuário da view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    

class ConsultaFormDentista(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'paciente', 'procedimentos']

    paciente = forms.ModelChoiceField(
        queryset = Cliente.objects.all(),
        required = True,
        label = "Paciente"
    )
    
    procedimentos = forms.ModelMultipleChoiceField(
        queryset = Procedimento.objects.all(),
        required = True,
        widget = forms.CheckboxSelectMultiple,
        label = "Procedimentos"
    )

    data = forms.DateField(widget=forms.SelectDateWidget, label="Data")
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Hora")

    def save(self,commit=True):
        consulta = super().save(commit=False)
                
        consulta.status = 'agendada'
        consulta.dentista = self.user.dentista

        if commit: 
            consulta.save()
        
            procedimentos_selecionados = self.cleaned_data['procedimentos']
            for procedimento in procedimentos_selecionados:
                consulta.procedimentos.add(procedimento)

            # consulta.procedimentos.set(procedimentos_selecionados)
            # procedimento_especifico = Procedimento.objects.get(nome="Consulta") 
            # consulta.procedimentos.add(procedimento_especifico)
            
        return consulta
    
    def __init__(self, *args, **kwargs):
        # Pega o usuário da view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)