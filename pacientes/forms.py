from django.forms import ModelForm
from django import forms
from .models import Cliente
from datetime import date

class ClienteForm(ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1900, date.today().year + 1)  # Anos de 1900 até o ano atual
        )
    )
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