from django.forms import ModelForm
from .models import Dentista

class DentistaForm(ModelForm):
    class Meta:
        model=Dentista
        fields=[
            'nome','cpf',
            'cro', 'especialidade',
            'telefone', 'salario',
            'data_contratacao','clinica',
            'endereco','numero_residencial',
        ]
        labels=[
            'Nome', 'CPF', 'CRO',
            'Especialidade', 'Telefone',
            'Salário', 'Data de contratação',
            'Clínica','Endereço','Número residencial',
        ]