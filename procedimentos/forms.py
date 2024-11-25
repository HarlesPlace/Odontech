from django.forms import ModelForm
from .models import Procedimento
# from django.contrib.auth import get_user_model

class ProcedimentoForm(ModelForm):
    class Meta:
        model=Procedimento
        fields=[
            'nome','descricao',
            'preco', 'custo',
            'duracao_media',
        ]
        labels=[
            'Nome', 'Descrição', 'Preço',
            'Custo',
            'Duração', 
        ]
