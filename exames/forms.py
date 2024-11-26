from django import forms
from .models import *
from pacientes.models import Cliente
from funcionarios.models import Dentista


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['data', 'status', 'cliente', 'dentista', 'exames']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)
    dentista = forms.ModelChoiceField(queryset=Dentista.objects.all(), required=True)
    exames = forms.ModelMultipleChoiceField(queryset=Exame.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)

    data = forms.DateField(widget=forms.SelectDateWidget)
    status = forms.ChoiceField(choices=[('pendente', 'Pendente'), 
                                        ('realizado', 'Realizado')], 
                                        required=True)
