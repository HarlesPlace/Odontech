from django import forms
from .models import *
from pacientes.models import Cliente
from funcionarios.models import Dentista


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['data', 'status', 'cliente', 'dentista', 'exames']

    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), 
        required=True,
        label="Paciente")
    
    dentista = forms.ModelChoiceField(
        queryset=Dentista.objects.all(), 
        required=True,
        label="Dentista")
    
    exames = forms.ModelMultipleChoiceField(
        queryset=Exame.objects.all(), 
        required=True, 
        widget=forms.CheckboxSelectMultiple,
        label="Exames")

    data = forms.DateField(widget=forms.SelectDateWidget)
    status = forms.ChoiceField(choices=[('pendente', 'Pendente'), 
                                        ('realizado', 'Realizado')], 
                                        required=True)
    
    def __init__(self, *args, **kwargs):
        # Pega os argumentos do view para verificar se devemos desabilitar campos
        disabled_fields = kwargs.pop('disabled_fields', [])
        super().__init__(*args, **kwargs)

        # Desabilita os campos conforme necessário
        for field in disabled_fields:
            if field in self.fields:
                self.fields[field].widget.attrs['disabled'] = 'disabled'
                self.fields[field].required = False  # Torna o campo não obrigatório
