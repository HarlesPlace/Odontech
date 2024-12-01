from django import forms
from .models import *
from pacientes.models import Cliente
from funcionarios.models import Dentista


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['data', 'cliente', 'dentista', 'exames', 'status']

    cliente = forms.ModelChoiceField(
        queryset = Cliente.objects.all(), 
        required = True,
        label = "Paciente")
    
    dentista = forms.ModelChoiceField(
        queryset = Dentista.objects.all(), 
        required = True,
        label = "Dentista")
    
    exames = forms.ModelMultipleChoiceField(
        queryset = Exame.objects.all(), 
        required = True, 
        widget = forms.CheckboxSelectMultiple,
        label = "Exames")

    data = forms.DateField(widget=forms.SelectDateWidget)
    status = forms.ChoiceField(choices=[('pendente', 'Pendente'), 
                                        ('realizado', 'Realizado')], 
                                        required=True)
    
    def save(self,commit=True):
        pedido = super().save(commit=False)
                
        

        if commit: 
            pedido.save()

            exames_selecionados = self.cleaned_data['exames']
            pedido.exames.set(exames_selecionados)

        return pedido
    
    def __init__(self, *args, **kwargs):
        # Pega o usuário da view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


class PedidoFormDentista(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['data', 'cliente', 'exames']

    cliente = forms.ModelChoiceField(
        queryset = Cliente.objects.all(), 
        required = True,
        label = "Paciente")
    
    exames = forms.ModelMultipleChoiceField(
        queryset = Exame.objects.all(), 
        required = True, 
        widget = forms.CheckboxSelectMultiple,
        label = "Exames")

    data = forms.DateField(widget=forms.SelectDateWidget)
    
    def save(self,commit=True):
        pedido=super().save(commit=False)
                
        pedido.status = 'pendente'
        pedido.dentista = self.user.dentista
        
        if commit: 
            pedido.save()

            exames_selecionados = self.cleaned_data['exames']
            pedido.exames.set(exames_selecionados)

        return pedido
    
    def __init__(self, *args, **kwargs):
        # Pega o usuário da view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
