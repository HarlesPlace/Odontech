from django.forms import ModelForm
from django import forms
from .models import Cliente

class ClienteForm(ModelForm):
    data_nascimento = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Cliente
        fields=[
            'nome','cpf',
            'telefone',
            'data_nascimento',
            'rua','numero_residencial',
            'bairro','cep','cidade','estado',
        ]
        labels=[
            'Nome', 'CPF', 
            'Telefone',
            'Nascimento',
            'Rua','Numero residencial',
            'Bairro','CEP','Cidade','Estado',
        ]